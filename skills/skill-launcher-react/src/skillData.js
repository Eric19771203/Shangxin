export const skillData = {
  categories: [
    {
      id: "novel",
      name: "小说创作",
      icon: "📖",
      skills: [
        { id: "SKILL-001", name: "古代权谋小说", type: "directory", path: "AI写小说/古代权谋类 短篇小说 Claude Skill/gudai-skill/SKILL.md", description: "文白相济风格的古代权谋小说创作", tags: ["小说", "古代", "权谋", "短篇"], features: ["大纲生成", "人物创作", "章节写作"] },
        { id: "SKILL-002", name: "现代言情小说", type: "directory", path: "AI写小说/现代言情类 短篇小说 Claude Skill/xianyan-skill/SKILL.md", description: "流畅自然风格的现代言情小说创作", tags: ["小说", "现代", "言情", "短篇"], features: ["大纲生成", "人物创作", "章节写作"] },
        { id: "SKILL-003", name: "现实题材小说", type: "directory", path: "AI写小说/现实题材类 短篇小说 Claude Skill/xianshi-skill/SKILL.md", description: "真实细腻风格的现实题材小说创作", tags: ["小说", "现实", "职场", "短篇"], features: ["大纲生成", "人物创作", "章节写作"] },
        { id: "novel-shiqing", name: "世情文短篇小说", type: "file", path: "AI写小说/小说 _ 世情文短篇小说提示词框架.md", description: "世情文风格短篇小说创作框架", tags: ["小说", "世情", "短篇"] },
        { id: "novel-expert", name: "AI小说创作专家", type: "file", path: "AI小说创作专家-SKILL.md", description: "专业AI小说创作指导", tags: ["小说", "AI", "创作"] },
        { id: "story-architect", name: "故事架构大师", type: "file", path: "1.【故事架构大师】系统提示词.txt", description: "专业的故事架构设计系统", tags: ["架构", "故事", "大纲"] }
      ]
    },
    {
      id: "drama",
      name: "短剧创作",
      icon: "🎬",
      skills: [
        { id: "SKILL-007", name: "末世重生漫剧", type: "directory", path: "末世重生类漫剧剧本创作 SKill/doomsday-skill/SKILL.md", description: "紧张刺激风格的末世重生漫剧创作", tags: ["短剧", "末世", "重生", "漫剧"], features: ["60集大纲", "人物设定", "分集剧本"] },
        { id: "SKILL-008", name: "玄幻类漫剧", type: "directory", path: "玄幻类漫剧剧本创作 Claude Skill/xuanhuan-skill/SKILL.md", description: "大气磅礴风格的玄幻漫剧创作", tags: ["短剧", "玄幻", "修仙", "漫剧"], features: ["世界观", "人物设定", "分集剧本"] },
        { id: "SKILL-009", name: "网文改编漫剧", type: "directory", path: "网文改编漫剧 Claude Agent +Skill/网文改编资料包/webtoon-skill/SKILL.md", description: "视觉化风格的网文改编漫剧创作", tags: ["短剧", "网文", "IP", "漫剧"], features: ["IP分析", "视觉转化", "分集剧本"] },
        { id: "drama-shuangwen", name: "爽文短剧", type: "file", path: "AI短剧/剧本 _ 爽文短剧提示词框架.md", description: "爽文风格短剧创作框架", tags: ["短剧", "爽文", "快节奏"] },
        { id: "drama-assistant", name: "影视编剧助理", type: "file", path: "AI短剧/影视 _ 影视编剧助理提示词框架.md", description: "专业影视编剧辅助工具", tags: ["编剧", "助理", "影视"] }
      ]
    },
    {
      id: "storyboard",
      name: "分镜设计",
      icon: "🎥",
      skills: [
        { id: "SKILL-004", name: "电影分镜", type: "directory", path: "AI 分镜师 配置文件/film-storyboard-skill/SKILL.md", description: "专业电影语言的分镜设计", tags: ["分镜", "电影", "剧情"], features: ["镜头设计", "运镜指导", "AI生图"] },
        { id: "SKILL-005", name: "动画分镜", type: "directory", path: "AI 分镜师 配置文件/animator-skill/SKILL.md.md", description: "动画特有的分镜设计", tags: ["分镜", "动画", "番剧"], features: ["动画语言", "动作设计", "AI生图"] },
        { id: "SKILL-006", name: "分镜评审", type: "directory", path: "AI 分镜师 配置文件/storyboard-review-skill/storyboard-review-skill-SKILL.md", description: "专业的分镜质量评审", tags: ["分镜", "评审", "质量"], features: ["质量检查", "优化建议", "标准对齐"] },
        { id: "SKILL-010", name: "TVC故事板创作器", type: "directory", path: "tvc-storyboard-creator/SKILL.md", description: "交互式TVC广告故事板生成器", tags: ["TVC", "广告", "故事板", "交互式"], features: ["19+交互点", "15+风格", "AI生图", "多区域"] },
        { id: "storyboard-jiugongge", name: "九宫格分镜图", type: "file", path: "九宫格分镜图-SKILL.md", description: "九宫格分镜图生成工具", tags: ["分镜", "九宫格", "视觉"] },
        { id: "storyboard-master", name: "分镜头大师", type: "file", path: "提示词Skills/09-分镜头大师-SKILL.md", description: "专业分镜头设计大师", tags: ["分镜", "大师", "专业"] },
        { id: "storyboard-v5", name: "影视工业化分镜架构师", type: "file", path: "【V5.2 影视工业化分镜架构师专业提示词系统】.txt", description: "V5.2影视工业化分镜系统", tags: ["分镜", "工业化", "专业"] },
        { id: "storyboard-holographic", name: "全息影视分镜生成引擎", type: "file", path: "7. 终极全息影视分镜生成引擎.txt", description: "全息影视分镜生成系统", tags: ["分镜", "全息", "引擎"] },
        { id: "storyboard-visual", name: "视觉叙事与分镜头生成", type: "file", path: "6. AI 视觉叙事与分镜头生成系统 (终极版).txt", description: "AI视觉叙事分镜生成系统", tags: ["分镜", "视觉", "叙事"] }
      ]
    },
    {
      id: "video",
      name: "视频生成",
      icon: "🎞️",
      skills: [
        { id: "seedance2", name: "Seedance 2.0", type: "directory", path: "seedance2-skill/SKILL.md", description: "Seedance 2.0视频生成技能", tags: ["视频", "Seedance", "AI"] },
        { id: "seedance-ultimate", name: "Seedance Ultimate", type: "directory", path: "SeedanceUltimateSkillSet/seedance-ultimate-skill/SKILL.md", description: "Seedance终极技能集", tags: ["视频", "Seedance", "终极"] },
        { id: "seedance-unified", name: "Seedance统一技能", type: "directory", path: "Seedance_Unified_Skill/Seedance_Unified_Master_Skill.md", description: "Seedance统一主技能", tags: ["视频", "Seedance", "统一"] },
        { id: "sora-builder", name: "Sora提示词构建", type: "file", path: "Sora提示词构建-SKILL.md", description: "Sora视频提示词构建工具", tags: ["视频", "Sora", "提示词"] },
        { id: "video-orchestrator", name: "视频提示词编排", type: "file", path: "提示词Skills/视频提示词编排-SKILL.md", description: "视频提示词编排工具", tags: ["视频", "提示词", "编排"] }
      ]
    },
    {
      id: "style",
      name: "风格预设",
      icon: "🎨",
      skills: [
        { id: "style-3d", name: "三维动画风格", type: "file", path: "三维动画风格-SKILL.md", description: "3D动画视觉风格预设", tags: ["风格", "3D", "动画"] },
        { id: "style-2d", name: "二次元动漫风格", type: "file", path: "二次元动漫风格-SKILL.md", description: "2D动漫视觉风格预设", tags: ["风格", "2D", "动漫"] },
        { id: "style-live", name: "真人实拍风格", type: "file", path: "提示词Skills/真人实拍风格-SKILL.md", description: "真人实拍视觉风格预设", tags: ["风格", "实拍", "真人"] },
        { id: "style-ancient", name: "古装历史剧风格", type: "file", path: "提示词Skills/古装历史剧风格-SKILL.md", description: "古装历史剧视觉风格预设", tags: ["风格", "古装", "历史"] },
        { id: "style-urban", name: "现代都市剧风格", type: "file", path: "提示词Skills/现代都市剧风格-SKILL.md", description: "现代都市剧视觉风格预设", tags: ["风格", "都市", "现代"] },
        { id: "style-campus", name: "校园青春剧风格", type: "file", path: "提示词Skills/校园青春剧风格-SKILL.md", description: "校园青春剧视觉风格预设", tags: ["风格", "校园", "青春"] },
        { id: "style-comedy", name: "喜剧搞笑剧风格", type: "file", path: "提示词Skills/喜剧搞笑剧风格-SKILL.md", description: "喜剧搞笑剧视觉风格预设", tags: ["风格", "喜剧", "搞笑"] },
        { id: "style-scifi", name: "奇幻科幻剧风格", type: "file", path: "提示词Skills/奇幻科幻剧风格-SKILL.md", description: "奇幻科幻剧视觉风格预设", tags: ["风格", "科幻", "奇幻"] },
        { id: "style-light", name: "光影风格", type: "file", path: "提示词Skills/光影风格-SKILL.md", description: "光影效果风格预设", tags: ["风格", "光影", "效果"] },
        { id: "style-color", name: "色调风格", type: "file", path: "提示词Skills/色调风格-SKILL.md", description: "色调配色风格预设", tags: ["风格", "色调", "配色"] },
        { id: "style-composition", name: "构图风格", type: "file", path: "提示词Skills/构图风格-SKILL.md", description: "画面构图风格预设", tags: ["风格", "构图", "画面"] }
      ]
    },
    {
      id: "character",
      name: "角色设计",
      icon: "👤",
      skills: [
        { id: "character-creator", name: "角色创建专家", type: "file", path: "提示词Skills/20-角色创建专家-SKILL.md", description: "专业角色创建工具", tags: ["角色", "创建", "设计"] },
        { id: "character-ip", name: "IP角色设定模板", type: "file", path: "IP角色设定模板-SKILL.md", description: "IP角色设定模板工具", tags: ["角色", "IP", "设定"] },
        { id: "character-casting", name: "角色开发与选角指南", type: "file", path: "2. 影视级角色开发与选角指南系统.txt", description: "影视级角色开发和选角系统", tags: ["角色", "开发", "选角"] },
        { id: "character-makeup", name: "电影人物定妆生成", type: "file", path: "3. 终极电影人物定妆生成系统.txt", description: "电影级人物定妆生成系统", tags: ["角色", "定妆", "电影"] },
        { id: "character-threeview", name: "三视图生成", type: "file", path: "三视图-SKILL.md", description: "角色三视图生成工具", tags: ["角色", "三视图", "设计"] },
        { id: "character-expression", name: "九宫格表情", type: "file", path: "九宫格表情-SKILL.md", description: "九宫格表情生成工具", tags: ["角色", "表情", "九宫格"] }
      ]
    },
    {
      id: "worldbuilding",
      name: "世界观",
      icon: "🌍",
      skills: [
        { id: "world-skillset", name: "世界观搭建SkillSet", type: "directory", path: "世界观搭建SkillSet/world-building-skill/SKILL.md", description: "完整的世界观搭建技能集", tags: ["世界观", "搭建", "设定"], features: ["核心概念", "场景设计", "角色绑定"] },
        { id: "world-building", name: "世界观搭建", type: "file", path: "世界观搭建.md", description: "世界观搭建工具", tags: ["世界观", "搭建"] }
      ]
    },
    {
      id: "review",
      name: "评审优化",
      icon: "✅",
      skills: [
        { id: "review-skillset", name: "专家评审SkillSet", type: "directory", path: "专家评审SkillSet/expert-review-skill/SKILL.md", description: "多领域专家评审技能集", tags: ["评审", "专家", "优化"], features: ["艺术创作", "时尚创意", "商业合规", "心理学"] },
        { id: "review-tuan", name: "全域审美与创作专业评审团", type: "directory", path: "全域审美与创作专业评审团/主编排器-MasterOrchestrator.md", description: "专业评审团系统", tags: ["评审", "专业", "审美"] },
        { id: "review-analyzer", name: "创意分析器", type: "file", path: "提示词Skills/03-创意分析器-SKILL.md", description: "创意可行性分析工具", tags: ["分析", "创意", "评估"] },
        { id: "review-optimizer", name: "分镜参数优化", type: "file", path: "分镜参数优化-SKILL.md", description: "分镜参数优化工具", tags: ["优化", "分镜", "参数"] }
      ]
    },
    {
      id: "postproduction",
      name: "后期制作",
      icon: "✨",
      skills: [
        { id: "post-effects", name: "AI后期特效与画质修复", type: "file", path: "终极 AI 后期特效与画质修复专家.txt", description: "AI后期特效和画质修复系统", tags: ["后期", "特效", "修复"] },
        { id: "post-sound", name: "动态导演与声景工程", type: "file", path: "终极 AI 动态导演与声景工程系统.txt", description: "动态导演和声景工程系统", tags: ["导演", "声景", "音频"] },
        { id: "post-consistency", name: "视觉一致性控制中枢", type: "file", path: "5. 终极视觉一致性控制中枢.txt", description: "视觉一致性控制系统", tags: ["视觉", "一致性", "控制"] },
        { id: "post-keyframe", name: "电影级关键帧原画生成", type: "file", path: "8. 终极电影级关键帧原画生成系统.txt", description: "电影级关键帧原画生成系统", tags: ["关键帧", "原画", "电影"] },
        { id: "post-environment", name: "电影空镜美术师", type: "file", path: "4. 终极电影空镜美术师 & 环境叙事大师.txt", description: "电影空镜和环境叙事系统", tags: ["空镜", "环境", "美术"] },
        { id: "post-image", name: "图像恢复", type: "file", path: "提示词Skills/图像恢复-SKILL.md", description: "图像修复和恢复工具", tags: ["图像", "恢复", "修复"] },
        { id: "post-editing", name: "剪辑思维与视觉桥接", type: "file", path: "【创世架构师】已启动'剪辑思维 (Editorial Thinking.txt", description: "剪辑思维和视觉桥接系统", tags: ["剪辑", "思维", "桥接"] }
      ]
    },
    {
      id: "tools",
      name: "其他工具",
      icon: "🛠️",
      skills: [
        { id: "tool-optimizer", name: "Skill架构优化器", type: "directory", path: "Skill-Architect-Optimizer/SKILL.md", description: "Skill架构优化工具", tags: ["Skill", "架构", "优化"] },
        { id: "tool-textdetect", name: "图像文字检测", type: "file", path: "提示词Skills/图像文字检测-SKILL.md", description: "图像中文字检测工具", tags: ["图像", "文字", "检测"] },
        { id: "tool-sensitive", name: "去敏感词", type: "file", path: "提示词Skills/去敏感词-SKILL.md", description: "敏感词过滤工具", tags: ["敏感词", "过滤", "文本"] },
        { id: "tool-outline", name: "剧本大纲规划", type: "file", path: "提示词Skills/剧本大纲规划-SKILL.md", description: "剧本大纲规划工具", tags: ["剧本", "大纲", "规划"] },
        { id: "tool-episode", name: "剧本分集", type: "file", path: "提示词Skills/剧本分集-SKILL.md", description: "剧本分集工具", tags: ["剧本", "分集"] },
        { id: "tool-extract", name: "角色提取", type: "file", path: "提示词Skills/角色提取-SKILL.md", description: "角色信息提取工具", tags: ["角色", "提取"] },
        { id: "tool-analysis", name: "剧目分析", type: "file", path: "提示词Skills/剧目分析-SKILL.md", description: "剧目分析工具", tags: ["剧目", "分析"] }
      ]
    }
  ]
};

export const getStats = () => {
  let totalSkills = 0;
  let directorySkills = 0;
  let fileSkills = 0;
  
  skillData.categories.forEach(cat => {
    totalSkills += cat.skills.length;
    cat.skills.forEach(skill => {
      if (skill.type === 'directory') directorySkills++;
      else fileSkills++;
    });
  });
  
  return {
    totalSkills,
    totalCategories: skillData.categories.length,
    directorySkills,
    fileSkills
  };
};
