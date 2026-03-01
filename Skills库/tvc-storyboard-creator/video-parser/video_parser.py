"""
TVC视频链接解析器
支持YouTube、Bilibili、抖音、TikTok等平台
"""

import os
import re
import json
import tempfile
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from urllib.parse import urlparse, parse_qs
import cv2
import yt_dlp
from PIL import Image
import requests


@dataclass
class VideoInfo:
    """视频信息数据结构"""

    platform: str
    title: str
    duration: int  # 秒
    uploader: str
    view_count: int
    description: str
    thumbnail_url: str
    video_url: str
    subtitles: Optional[str] = None


@dataclass
class FrameAnalysis:
    """关键帧分析"""

    timestamp: float
    frame_path: str
    dominant_colors: List[str]
    brightness: float
    has_text: bool
    composition_type: str  # symmetrical, rule_of_thirds, center


class TVCVideoParser:
    """TVC视频链接解析器主类"""

    def __init__(self, temp_dir: str = None):
        self.temp_dir = temp_dir or tempfile.mkdtemp()
        self.ydl_opts = {
            "format": "best[height<=720]",  # 限制分辨率，节省带宽
            "outtmpl": f"{self.temp_dir}/%(title)s.%(ext)s",
            "quiet": True,
            "no_warnings": True,
        }

    def identify_platform(self, url: str) -> str:
        """识别视频平台"""
        domain = urlparse(url).netloc.lower()

        if any(x in domain for x in ["youtube", "youtu.be"]):
            return "youtube"
        elif "bilibili" in domain or "b23.tv" in domain:
            return "bilibili"
        elif "douyin" in domain:
            return "douyin"
        elif "tiktok" in domain:
            return "tiktok"
        elif "xiaohongshu" in domain or "xhs.link" in domain:
            return "xiaohongshu"
        elif "weibo" in domain:
            return "weibo"
        else:
            return "unknown"

    def extract_video_id(self, url: str, platform: str) -> Optional[str]:
        """提取视频ID"""
        if platform == "youtube":
            # YouTube ID提取
            parsed = urlparse(url)
            if parsed.netloc == "youtu.be":
                return parsed.path[1:]
            return parse_qs(parsed.query).get("v", [None])[0]

        elif platform == "bilibili":
            # B站BV号提取
            match = re.search(r"BV[a-zA-Z0-9]{10}", url)
            if match:
                return match.group()
            # 也可能是av号
            match = re.search(r"av(\d+)", url)
            if match:
                return f"av{match.group(1)}"

        elif platform == "douyin":
            # 抖音视频ID（在URL路径中）
            match = re.search(r"/video/(\d+)", url)
            if match:
                return match.group(1)

        elif platform == "tiktok":
            # TikTok视频ID
            match = re.search(r"/video/(\d+)", url)
            if match:
                return match.group(1)

        return None

    def fetch_video_info(self, url: str) -> VideoInfo:
        """获取视频信息（不下载完整视频）"""
        platform = self.identify_platform(url)

        try:
            with yt_dlp.YoutubeDL({"quiet": True}) as ydl:
                info = ydl.extract_info(url, download=False)

                return VideoInfo(
                    platform=platform,
                    title=info.get("title", "Unknown"),
                    duration=int(info.get("duration", 0)),
                    uploader=info.get("uploader", "Unknown"),
                    view_count=info.get("view_count", 0),
                    description=info.get("description", ""),
                    thumbnail_url=info.get("thumbnail", ""),
                    video_url=url,
                )
        except Exception as e:
            print(f"Error fetching info: {e}")
            return VideoInfo(
                platform=platform,
                title="Unknown",
                duration=0,
                uploader="Unknown",
                view_count=0,
                description="",
                thumbnail_url="",
                video_url=url,
            )

    def download_video(self, url: str, max_duration: int = 120) -> Optional[str]:
        """
        下载视频（限制时长，TVC通常很短）

        Args:
            url: 视频链接
            max_duration: 最大下载时长（秒），TVC通常30-60秒

        Returns:
            本地视频文件路径
        """
        try:
            # 先获取信息检查时长
            info = self.fetch_video_info(url)
            if info.duration > max_duration:
                print(f"Warning: Video is {info.duration}s, longer than typical TVC")
                # 仍然下载，但标记为长视频

            # 下载视频
            opts = self.ydl_opts.copy()
            opts["format"] = "best[filesize<50M]"  # 限制文件大小

            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
                return filename

        except Exception as e:
            print(f"Error downloading video: {e}")
            return None

    def extract_keyframes(
        self, video_path: str, num_frames: int = 8
    ) -> List[FrameAnalysis]:
        """
        提取关键帧用于视觉分析

        Args:
            video_path: 本地视频路径
            num_frames: 提取帧数（默认8张，覆盖开头/中间/结尾）

        Returns:
            帧分析结果列表
        """
        frames = []

        try:
            cap = cv2.VideoCapture(video_path)
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            duration = total_frames / fps

            # 均匀采样时间点
            timestamps = [i * duration / (num_frames - 1) for i in range(num_frames)]

            for i, timestamp in enumerate(timestamps):
                frame_number = int(timestamp * fps)
                cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
                ret, frame = cap.read()

                if ret:
                    # 保存帧
                    frame_path = f"{self.temp_dir}/frame_{i:02d}_{timestamp:.1f}s.jpg"
                    cv2.imwrite(frame_path, frame)

                    # 分析帧
                    analysis = self._analyze_frame(frame, frame_path, timestamp)
                    frames.append(analysis)

            cap.release()

        except Exception as e:
            print(f"Error extracting frames: {e}")

        return frames

    def _analyze_frame(self, frame, frame_path: str, timestamp: float) -> FrameAnalysis:
        """分析单帧的视觉特征"""
        # 转换到PIL进行颜色分析
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(frame_rgb)

        # 提取主色调（简化版，实际可用K-means聚类）
        small_image = pil_image.resize((50, 50))
        pixels = list(small_image.getdata())
        # 取最常见的几个颜色（简化）
        colors = self._extract_dominant_colors(pixels, n_colors=3)

        # 亮度分析
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        brightness = float(gray.mean())

        # 构图分析（简化）
        height, width = frame.shape[:2]
        composition = self._analyze_composition(frame, height, width)

        return FrameAnalysis(
            timestamp=timestamp,
            frame_path=frame_path,
            dominant_colors=colors,
            brightness=brightness,
            has_text=False,  # 需要OCR检测
            composition_type=composition,
        )

    def _extract_dominant_colors(self, pixels: List, n_colors: int = 3) -> List[str]:
        """提取主色调（简化实现）"""
        # 实际实现应使用K-means聚类
        # 这里简化处理，取平均色
        if not pixels:
            return ["#000000"]

        r_sum = sum(p[0] for p in pixels) // len(pixels)
        g_sum = sum(p[1] for p in pixels) // len(pixels)
        b_sum = sum(p[2] for p in pixels) // len(pixels)

        return [f"#{r_sum:02x}{g_sum:02x}{b_sum:02x}"]

    def _analyze_composition(self, frame, height: int, width: int) -> str:
        """分析构图类型"""
        # 简化：检测对称性
        # 实际应使用更复杂的图像分析

        # 垂直对称检测
        left_half = frame[:, : width // 2]
        right_half = cv2.flip(frame[:, width // 2 :], 1)
        diff = cv2.absdiff(left_half, right_half)
        symmetry_score = 1 - (diff.mean() / 255)

        if symmetry_score > 0.8:
            return "symmetrical"
        else:
            return "asymmetrical"

    def extract_subtitles(self, url: str) -> Optional[str]:
        """提取视频字幕/旁白"""
        platform = self.identify_platform(url)

        try:
            if platform == "youtube":
                # 使用youtube-transcript-api
                from youtube_transcript_api import YouTubeTranscriptApi

                video_id = self.extract_video_id(url, platform)
                if video_id:
                    transcript = YouTubeTranscriptApi.get_transcript(video_id)
                    return " ".join([item["text"] for item in transcript])

            # 其他平台可通过yt-dlp获取自动字幕
            opts = {
                "skip_download": True,
                "writesubtitles": True,
                "writeautomaticsub": True,
                "subtitleslangs": ["zh", "en", "zh-CN", "zh-TW"],
                "quiet": True,
            }

            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=False)
                # 字幕会在下载目录生成，需要读取
                # 简化处理，实际需解析字幕文件
                return info.get("description", "")  # 暂时返回描述

        except Exception as e:
            print(f"Error extracting subtitles: {e}")
            return None

    def parse_tvc(self, url: str, download: bool = True) -> Dict:
        """
        解析TVC的完整流程

        Args:
            url: 视频链接
            download: 是否下载完整视频进行分析

        Returns:
            完整的分析报告
        """
        print(f"🔍 开始解析: {url}")

        # 1. 识别平台
        platform = self.identify_platform(url)
        print(f"📺 平台识别: {platform}")

        # 2. 获取视频信息
        print("📊 获取视频信息...")
        video_info = self.fetch_video_info(url)
        print(f"✓ 标题: {video_info.title}")
        print(f"✓ 时长: {video_info.duration}秒")
        print(f"✓ 作者: {video_info.uploader}")

        # 3. 提取字幕/描述
        print("📝 提取字幕...")
        subtitles = self.extract_subtitles(url)

        result = {
            "url": url,
            "platform": platform,
            "video_info": {
                "title": video_info.title,
                "duration": video_info.duration,
                "uploader": video_info.uploader,
                "view_count": video_info.view_count,
                "description": video_info.description[:500],  # 截断
            },
            "subtitles": subtitles,
            "frames": [],
        }

        # 4. 如果需要详细分析，下载视频
        if download and video_info.duration <= 180:  # 只分析3分钟以内的视频
            print("⬇️  下载视频进行分析...")
            video_path = self.download_video(url)

            if video_path:
                print("🎬 提取关键帧...")
                frames = self.extract_keyframes(video_path, num_frames=8)

                result["frames"] = [
                    {
                        "timestamp": f.frame,
                        "frame_path": f.frame_path,
                        "dominant_colors": f.dominant_colors,
                        "brightness": round(f.brightness, 2),
                        "composition": f.composition_type,
                    }
                    for f in frames
                ]

                print(f"✓ 成功提取 {len(frames)} 个关键帧")

                # 清理临时文件
                # os.remove(video_path)  # 保留供后续分析

        print("✅ 解析完成!")
        return result


# 使用示例
if __name__ == "__main__":
    parser = TVCVideoParser()

    # 测试URL
    test_urls = [
        # YouTube示例（需替换为实际TVC链接）
        "https://www.youtube.com/watch?v=example",
        # B站示例
        "https://www.bilibili.com/video/BV1xx411c7mD",
    ]

    for url in test_urls:
        print("\n" + "=" * 60)
        try:
            result = parser.parse_tvc(url, download=False)  # 先不下载，只获取信息
            print(json.dumps(result, indent=2, ensure_ascii=False))
        except Exception as e:
            print(f"Error: {e}")
