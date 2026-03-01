"""
TVC广告片分类知识库模块
包含产品功能型、品牌故事型、促销型、企业形象型等
"""

from typing import List, Dict, Any


# 产品功能型广告知识库
class ProductTVCKnowledge:
    """TVC-产品功能型知识库"""
    
    CHARACTERISTICS = {
        "name": "TVC-产品功能型",
        "description": "突出产品功能、使用场景和效果展示",
        "key_elements": ["问题-解决方案", "产品展示", "效果对比", "使用场景", "功能演示"],
        "typical_duration": "15-30秒",
        "typical_shot_count": "8-15个镜头",
        "pacing": "快节奏，信息密度高"
    }
    
    # 经典结构：问题→解决方案→产品展示
    STRUCTURE = {
        "problem": {
            "duration": "3-5秒",
            "shots": "2-3个",
            "purpose": "建立痛点",
            "content": "展示问题场景，引发共鸣"
        },
        "solution_intro": {
            "duration": "3-5秒",
            "shots": "2-3个",
            "purpose": "引入产品",
            "content": "产品登场，引起好奇"
        },
        "product_demo": {
            "duration": "5-10秒",
            "shots": "3-5个",
            "purpose": "功能演示",
            "content": "展示产品功能和使用方法"
        },
        "result": {
            "duration": "3-5秒",
            "shots": "2-3个",
            "purpose": "效果展示",
            "content": "问题解决，满意结果"
        },
        "cta": {
            "duration": "2-3秒",
            "shots": "1个",
            "purpose": "行动号召",
            "content": "品牌logo，购买信息"
        }
    }
    
    SHOT_TECHNIQUES = {
        "product_hero": {
            "description": "产品英雄镜头",
            "lighting": "柔和均匀，突出质感",
            "background": "简洁干净",
            "angle": "多角度展示"
        },
        "macro_detail": {
            "description": "产品细节特写",
            "lens": "微距镜头",
            "purpose": "展示材质和工艺"
        },
        "lifestyle": {
            "description": "生活场景",
            "purpose": "展示使用场景",
            "style": "自然、真实"
        },
        "before_after": {
            "description": "前后对比",
            "technique": "分屏或快速切换",
            "purpose": "直观展示效果"
        }
    }
    
    STORYBOARD_3X3 = {
        "template_name": "产品广告功能3×3",
        "shots": [
            {
                "index": 1, 
                "name": "问题场景", 
                "shot_type": "中景",
                "duration": "2秒",
                "prompt": "Problem scenario, frustrated user, relatable situation, natural lighting, everyday setting, pain point establishment"
            },
            {
                "index": 2, 
                "name": "产品登场", 
                "shot_type": "全景",
                "duration": "1.5秒",
                "prompt": "Product entrance, hero shot, elegant packaging, attractive lighting, premium feel, solution introduction"
            },
            {
                "index": 3, 
                "name": "功能展示", 
                "shot_type": "中全景",
                "duration": "2秒",
                "prompt": "Product in use, hands interacting, function demonstration, clear view, user-friendly design"
            },
            {
                "index": 4, 
                "name": "特写效果", 
                "shot_type": "近景",
                "duration": "1.5秒",
                "prompt": "Product detail close-up, texture and quality, macro shot, premium materials, craftsmanship"
            },
            {
                "index": 5, 
                "name": "使用效果", 
                "shot_type": "中近景",
                "duration": "2秒",
                "prompt": "Satisfied user, positive reaction, result demonstration, happy expression, problem solved"
            },
            {
                "index": 6, 
                "name": "产品特写", 
                "shot_type": "特写",
                "duration": "1.5秒",
                "prompt": "Product beauty shot, perfect lighting, clean background, brand visibility, hero angle"
            },
            {
                "index": 7, 
                "name": "品牌元素", 
                "shot_type": "特写A",
                "duration": "1秒",
                "prompt": "Logo close-up, brand element, packaging detail, brand recognition, memorable visual"
            },
            {
                "index": 8, 
                "name": "满意表情", 
                "shot_type": "特写B",
                "duration": "1秒",
                "prompt": "Happy customer face, genuine smile, satisfaction guaranteed, close-up, positive emotion"
            },
            {
                "index": 9, 
                "name": "品牌收尾", 
                "shot_type": "全景",
                "duration": "2秒",
                "prompt": "Brand end frame, product with logo, tagline, call to action, clean composition, lasting impression"
            }
        ]
    }


# 品牌故事型广告知识库
class BrandTVCKnowledge:
    """TVC-品牌故事型知识库"""
    
    CHARACTERISTICS = {
        "name": "TVC-品牌故事型",
        "description": "讲述品牌故事，传递品牌价值和情感共鸣",
        "key_elements": ["情感共鸣", "品牌价值", "故事叙事", "记忆点", "品牌调性"],
        "typical_duration": "30-60秒",
        "typical_shot_count": "15-25个镜头",
        "pacing": "故事节奏，情绪递进"
    }
    
    # 品牌风格类型
    BRAND_STYLES = {
        "fresh_natural": {
            "name": "清新自然风",
            "colors": "绿、白、浅蓝",
            "mood": "纯净、健康、自然",
            "examples": "护肤品、食品"
        },
        "luxury_premium": {
            "name": "高级奢华风",
            "colors": "金、黑、深蓝",
            "mood": "高端、精致、尊贵",
            "examples": "奢侈品、汽车"
        },
        "youth_trendy": {
            "name": "年轻潮流风",
            "colors": "鲜艳、对比强",
            "mood": "活力、时尚、前卫",
            "examples": "运动品牌、饮料"
        },
        "warm_emotional": {
            "name": "温暖情感风",
            "colors": "暖黄、橙、粉",
            "mood": "温馨、感动、亲切",
            "examples": "家庭用品、保险"
        }
    }
    
    STORYBOARD_3X3 = {
        "template_name": "品牌故事情感3×3",
        "shots": [
            {
                "index": 1, 
                "name": "品牌世界", 
                "shot_type": "远景",
                "duration": "3秒",
                "prompt": "Brand world establishing shot, atmospheric location, brand color palette, cinematic quality, emotional setting"
            },
            {
                "index": 2, 
                "name": "人物登场", 
                "shot_type": "全景",
                "duration": "2.5秒",
                "prompt": "Character introduction, full body, personality aligned with brand, natural movement, brand lifestyle"
            },
            {
                "index": 3, 
                "name": "情感建立", 
                "shot_type": "中全景",
                "duration": "3秒",
                "prompt": "Emotional connection building, relationship moment, brand values in action, authentic interaction"
            },
            {
                "index": 4, 
                "name": "故事发展", 
                "shot_type": "中景",
                "duration": "3秒",
                "prompt": "Story development, narrative progression, brand role in life, meaningful moment, lifestyle integration"
            },
            {
                "index": 5, 
                "name": "情感高潮", 
                "shot_type": "中近景",
                "duration": "3秒",
                "prompt": "Emotional peak, brand moment of truth, heartfelt connection, touching scene, brand love"
            },
            {
                "index": 6, 
                "name": "品牌融入", 
                "shot_type": "近景",
                "duration": "2.5秒",
                "prompt": "Brand integration, product in emotional context, natural placement, lifestyle fit, seamless blend"
            },
            {
                "index": 7, 
                "name": "品牌符号", 
                "shot_type": "特写A",
                "duration": "2秒",
                "prompt": "Brand symbol close-up, iconic element, memorable visual, brand recognition, signature detail"
            },
            {
                "index": 8, 
                "name": "情感眼神", 
                "shot_type": "特写B",
                "duration": "2秒",
                "prompt": "Emotional eyes, connection with brand, genuine feeling, extreme close-up, soul connection"
            },
            {
                "index": 9, 
                "name": "品牌升华", 
                "shot_type": "远景",
                "duration": "3秒",
                "prompt": "Brand elevation wide shot, aspirational ending, brand promise fulfilled, lasting impression, tagline moment"
            }
        ]
    }


# 促销型广告知识库
class PromoTVCKnowledge:
    """TVC-促销型知识库"""
    
    CHARACTERISTICS = {
        "name": "TVC-促销型",
        "description": "强调优惠信息，制造紧迫感和购买冲动",
        "key_elements": ["价格突出", "限时紧迫", "优惠力度", "行动号召", "信息清晰"],
        "typical_duration": "10-20秒",
        "typical_shot_count": "5-10个镜头",
        "pacing": "极快，信息轰炸"
    }
    
    STORYBOARD_3X3 = {
        "template_name": "促销广告紧迫3×3",
        "shots": [
            {
                "index": 1, 
                "name": "产品展示", 
                "shot_type": "全景",
                "duration": "1.5秒",
                "prompt": "Product hero shot, attractive presentation, bright lighting, appealing angle, attention grabbing"
            },
            {
                "index": 2, 
                "name": "原价对比", 
                "shot_type": "中景",
                "duration": "1秒",
                "prompt": "Original price strike-through, comparison setup, value demonstration, clear typography"
            },
            {
                "index": 3, 
                "name": "促销价格", 
                "shot_type": "中近景",
                "duration": "1.5秒",
                "prompt": "Sale price highlight, big bold numbers, discount emphasis, attractive offer, eye-catching"
            },
            {
                "index": 4, 
                "name": "产品功能", 
                "shot_type": "中景",
                "duration": "1秒",
                "prompt": "Product benefit quick shot, feature flash, fast editing, information delivery"
            },
            {
                "index": 5, 
                "name": "限时紧迫", 
                "shot_type": "中近景",
                "duration": "1.5秒",
                "prompt": "Urgency element, limited time indicator, countdown or clock, scarcity message, act now"
            },
            {
                "index": 6, 
                "name": "赠品/优惠", 
                "shot_type": "近景",
                "duration": "1秒",
                "prompt": "Bonus or extra offer, additional value, gift visualization, more for less"
            },
            {
                "index": 7, 
                "name": "价格特写", 
                "shot_type": "特写A",
                "duration": "1秒",
                "prompt": "Price extreme close-up, biggest text, super deal emphasis, can't miss offer"
            },
            {
                "index": 8, 
                "name": "兴奋表情", 
                "shot_type": "特写B",
                "duration": "1秒",
                "prompt": "Excited customer face, thrilled expression, deal excitement, social proof, FOMO"
            },
            {
                "index": 9, 
                "name": "行动号召", 
                "shot_type": "全景",
                "duration": "2秒",
                "prompt": "Call to action end frame, contact info, store location, website, buy now message, final push"
            }
        ]
    }


# 企业形象型广告知识库
class CorporateTVCKnowledge:
    """TVC-企业形象型知识库"""
    
    CHARACTERISTICS = {
        "name": "TVC-企业形象型",
        "description": "展示企业实力、社会责任和愿景",
        "key_elements": ["企业实力", "社会责任", "愿景展示", "专业可信", "大气磅礴"],
        "typical_duration": "30-90秒",
        "typical_shot_count": "20-35个镜头",
        "pacing": "大气稳重，节奏适中"
    }
    
    STORYBOARD_3X3 = {
        "template_name": "企业形象大气3×3",
        "shots": [
            {
                "index": 1, 
                "name": "企业全景", 
                "shot_type": "大远景",
                "duration": "4秒",
                "prompt": "Corporate headquarters wide shot, impressive architecture, aerial view, scale and power, establishing grandeur"
            },
            {
                "index": 2, 
                "name": "员工群像", 
                "shot_type": "全景",
                "duration": "3秒",
                "prompt": "Diverse employees, professional team, corporate culture, human element, organizational strength"
            },
            {
                "index": 3, 
                "name": "工作场景", 
                "shot_type": "中全景",
                "duration": "3秒",
                "prompt": "Professional work environment, modern office, collaboration, productivity, corporate excellence"
            },
            {
                "index": 4, 
                "name": "技术/创新", 
                "shot_type": "中景",
                "duration": "3秒",
                "prompt": "Innovation showcase, technology in action, R&D environment, cutting-edge, forward-thinking"
            },
            {
                "index": 5, 
                "name": "领导/专家", 
                "shot_type": "中近景",
                "duration": "3秒",
                "prompt": "Leadership portrait, expert interview, confident professional, thought leadership, credibility"
            },
            {
                "index": 6, 
                "name": "社会责任", 
                "shot_type": "近景",
                "duration": "3秒",
                "prompt": "CSR moment, community involvement, environmental care, social impact, responsible corporate citizen"
            },
            {
                "index": 7, 
                "name": "企业标识", 
                "shot_type": "特写A",
                "duration": "2秒",
                "prompt": "Corporate logo close-up, brand identity, building signage, prestigious mark, brand pride"
            },
            {
                "index": 8, 
                "name": "愿景眼神", 
                "shot_type": "特写B",
                "duration": "2秒",
                "prompt": "Visionary gaze, looking to future, aspirational expression, determination, corporate vision"
            },
            {
                "index": 9, 
                "name": "企业愿景", 
                "shot_type": "远景",
                "duration": "4秒",
                "prompt": "Corporate vision wide shot, future horizon, aspirational ending, tagline display, lasting corporate image"
            }
        ]
    }


# 导出所有知识库
TVC_KNOWLEDGE_BASES = {
    "product": ProductTVCKnowledge,
    "brand": BrandTVCKnowledge,
    "promo": PromoTVCKnowledge,
    "corporate": CorporateTVCKnowledge,
}


def get_tvc_knowledge(tvc_type: str):
    """获取指定类型的TVC知识库"""
    return TVC_KNOWLEDGE_BASES.get(tvc_type)


def get_tvc_storyboard(tvc_type: str, board_type: str = "3x3"):
    """获取指定类型的分镜模板"""
    knowledge = get_tvc_knowledge(tvc_type)
    if knowledge:
        return knowledge.STORYBOARD_3X3
    return None


def list_tvc_types():
    """列出所有可用的TVC类型"""
    return list(TVC_KNOWLEDGE_BASES.keys())


__all__ = [
    'ProductTVCKnowledge',
    'BrandTVCKnowledge',
    'PromoTVCKnowledge',
    'CorporateTVCKnowledge',
    'get_tvc_knowledge',
    'get_tvc_storyboard',
    'list_tvc_types',
]
