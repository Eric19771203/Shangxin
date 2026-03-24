#!/bin/bash
# Seedance焚决项目组快速启动脚本

echo "🚀 启动 Seedance焚决融合引擎 v2.0 P0核心版"
echo "-----------------------------------"
echo "✅ 已融合焚决终结版 + 即梦2.0 V4.2增强版核心能力"
echo "✅ 全自动化流程，仅需输入剧本即可生成Seedance 2.0标准生产包"

case "$1" in
  "create")
    echo "🎬 创建新项目：$2"
    mkdir -p output/$2
    echo "✅ 项目 $2 已创建，目录：output/$2"
    ;;
  "director")
    echo "🎨 调用导演系统：$2"
    openclaw skill run src/seedance-director --prompt "$2"
    ;;
  "generate")
    echo "🎥 启动生成任务：$2"
    openclaw skill run src/fenjue-system --input "$2"
    ;;
  "status")
    echo "📊 项目状态："
    ls -la output/
    ;;
  *)
    echo "使用方法："
    echo "  ./run.sh create <项目名>    创建新项目"
    echo "  ./run.sh director <创意>     调用导演系统生成分镜"
    echo "  ./run.sh generate <分镜文件> 启动生成任务"
    echo "  ./run.sh status              查看项目状态"
    ;;
esac
