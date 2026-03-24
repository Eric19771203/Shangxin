import { useState, useMemo } from 'react';
import { skillData, getStats } from './skillData';
import './App.css';

function App() {
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedSkill, setSelectedSkill] = useState(null);
  const [copied, setCopied] = useState(false);

  const stats = useMemo(() => getStats(), []);

  const filteredCategories = useMemo(() => {
    if (!searchQuery && selectedCategory === 'all') {
      return skillData.categories;
    }

    return skillData.categories
      .map(cat => {
        if (selectedCategory !== 'all' && cat.id !== selectedCategory) {
          return null;
        }

        const filteredSkills = cat.skills.filter(skill => {
          if (!searchQuery) return true;
          const query = searchQuery.toLowerCase();
          return (
            skill.name.toLowerCase().includes(query) ||
            skill.description.toLowerCase().includes(query) ||
            skill.tags.some(tag => tag.toLowerCase().includes(query))
          );
        });

        if (filteredSkills.length === 0) return null;

        return { ...cat, skills: filteredSkills };
      })
      .filter(Boolean);
  }, [selectedCategory, searchQuery]);

  const handleSkillClick = (skill, category) => {
    setSelectedSkill({ ...skill, category });
  };

  const closeDetail = () => {
    setSelectedSkill(null);
    setCopied(false);
  };

  const launchSkill = async () => {
    if (!selectedSkill) return;
    
    const command = `SKILL_CALL ${selectedSkill.id}`;
    try {
      await navigator.clipboard.writeText(command);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch (err) {
      alert(`请手动复制以下命令：\n${command}`);
    }
  };

  return (
    <div className="app">
      <header className="header">
        <h1>🎯 Skill启动器 Pro</h1>
        <p>管理和使用您的所有AI创作技能</p>
        <div className="stats-bar">
          <div className="stat-item">
            <div className="stat-value">{stats.totalSkills}</div>
            <div className="stat-label">总技能数</div>
          </div>
          <div className="stat-item">
            <div className="stat-value">{stats.totalCategories}</div>
            <div className="stat-label">分类数</div>
          </div>
          <div className="stat-item">
            <div className="stat-value">{stats.directorySkills}</div>
            <div className="stat-label">目录技能</div>
          </div>
          <div className="stat-item">
            <div className="stat-value">{stats.fileSkills}</div>
            <div className="stat-label">文件技能</div>
          </div>
        </div>
      </header>

      <div className="container">
        <input
          type="text"
          className="search-box"
          placeholder="🔍 搜索技能（名称、描述、标签）..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        />

        <div className="tabs">
          <button
            className={`tab ${selectedCategory === 'all' ? 'active' : ''}`}
            onClick={() => setSelectedCategory('all')}
          >
            📚 全部
          </button>
          {skillData.categories.map(cat => (
            <button
              key={cat.id}
              className={`tab ${selectedCategory === cat.id ? 'active' : ''}`}
              onClick={() => setSelectedCategory(cat.id)}
            >
              {cat.icon} {cat.name}
            </button>
          ))}
        </div>

        <div className="skills-container">
          {filteredCategories.length === 0 ? (
            <div className="no-results">
              <div className="no-results-icon">🔍</div>
              <h3>没有找到匹配的技能</h3>
              <p>请尝试其他搜索关键词</p>
            </div>
          ) : (
            filteredCategories.map(cat => (
              <div key={cat.id} className="category-section">
                <div className="category-header">
                  <span className="category-icon">{cat.icon}</span>
                  <span className="category-title">{cat.name}</span>
                  <span className="category-count">{cat.skills.length} 个技能</span>
                </div>
                <div className="skill-grid">
                  {cat.skills.map(skill => (
                    <div
                      key={skill.id}
                      className="skill-card"
                      onClick={() => handleSkillClick(skill, cat)}
                    >
                      <div className="skill-header">
                        <span className="skill-name">{skill.name}</span>
                        <span className={`skill-type ${skill.type}`}>
                          {skill.type === 'directory' ? '📁 目录' : '📄 文件'}
                        </span>
                      </div>
                      <p className="skill-desc">{skill.description}</p>
                      <div className="skill-tags">
                        {skill.tags.slice(0, 4).map((tag, idx) => (
                          <span key={idx} className="skill-tag">{tag}</span>
                        ))}
                      </div>
                      {skill.features && (
                        <div className="skill-features">
                          {skill.features.slice(0, 3).map((feature, idx) => (
                            <span key={idx} className="feature-item">✓ {feature}</span>
                          ))}
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            ))
          )}
        </div>
      </div>

      {selectedSkill && (
        <>
          <div className="detail-overlay" onClick={closeDetail} />
          <div className="detail-panel">
            <button className="detail-close" onClick={closeDetail}>×</button>
            <div className="detail-content">
              <div className="detail-header">
                <h2 className="detail-title">{selectedSkill.name}</h2>
                <div className="detail-meta">
                  <span className={`detail-type ${selectedSkill.type}`}>
                    {selectedSkill.type === 'directory' ? '📁 目录类型' : '📄 文件类型'}
                  </span>
                  <span className="detail-category">
                    {selectedSkill.category.icon} {selectedSkill.category.name}
                  </span>
                </div>
              </div>

              <div className="detail-section">
                <h3>📝 技能描述</h3>
                <p>{selectedSkill.description}</p>
              </div>

              <div className="detail-section">
                <h3>🏷️ 标签</h3>
                <div className="detail-tags">
                  {selectedSkill.tags.map((tag, idx) => (
                    <span key={idx} className="detail-tag">{tag}</span>
                  ))}
                </div>
              </div>

              {selectedSkill.features && (
                <div className="detail-section">
                  <h3>✨ 功能特性</h3>
                  <div className="detail-features">
                    {selectedSkill.features.map((feature, idx) => (
                      <div key={idx} className="detail-feature">{feature}</div>
                    ))}
                  </div>
                </div>
              )}

              <div className="detail-section">
                <h3>📂 文件路径</h3>
                <code className="detail-path">{selectedSkill.path}</code>
              </div>

              <button
                className={`launch-btn ${copied ? 'copied' : ''}`}
                onClick={launchSkill}
              >
                {copied ? '✅ 已复制到剪贴板' : '🚀 启动 Skill'}
              </button>
            </div>
          </div>
        </>
      )}
    </div>
  );
}

export default App;
