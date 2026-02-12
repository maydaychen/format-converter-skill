# 格式转换工具包 (Format Converter)

一个强大的格式转换技能包，专为Moltbot设计，用于处理各种常见的文档格式转换任务。

## 🚀 主要功能

### Markdown 转 PDF
- 将Markdown文件转换为专业PDF文档
- 支持中英文混合内容
- 自动生成目录和章节编号
- 代码块语法高亮
- 支持自定义样式和模板

## 📁 目录结构

```
format-converter/
├── SKILL.md                 # 技能元数据和描述
├── README.md               # 英文使用说明
├── README_zh.md            # 中文使用说明
├── scripts/
│   └── md_to_pdf.py        # Markdown转PDF核心脚本
└── references/
    └── usage_examples.md   # 使用示例和最佳实践
```

## ⚙️ 安装依赖

确保系统已安装以下依赖：

```bash
# 安装pandoc（文档转换工具）
sudo yum install pandoc

# 安装TeX Live（LaTeX排版系统）
sudo yum install texlive-collection-basic \
                 texlive-collection-fontsrecommended \
                 texlive-collection-latex
```

## 🎯 使用方法

### 基本用法
```bash
cd scripts/
python3 md_to_pdf.py 输入文件.md 输出文件.pdf
```

### 高级选项
```bash
# 使用自定义CSS样式
python3 md_to_pdf.py --css 样式.css 输入.md 输出.pdf

# 使用自定义LaTeX模板
python3 md_to_pdf.py --template 模板.latex 输入.md 输出.pdf
```

## 🌟 特性亮点

- **高质量输出**: 使用专业的LaTeX排版引擎
- **多语言支持**: 完美支持中文、英文及其他语言
- **灵活定制**: 可通过CSS或LaTeX模板自定义样式
- **错误处理**: 完善的错误提示和异常处理
- **批量处理**: 易于集成到自动化工作流中

## 📝 使用示例

### 创建简单文档
```markdown
# 我的文档

这是一个**重要的**段落。

```python
print("Hello, World!")
```

## 第二章节

更多内容...
```

运行转换：
```bash
python3 md_to_pdf.py my_doc.md my_doc.pdf
```

### 中文文档支持
```markdown
# 测试文档

这是一个包含中文的文档示例。

代码示例：
```javascript
const message = "你好，世界！";
console.log(message);
```
```

## 🔧 故障排除

### 常见问题

**Q: 转换中文时出现编码错误**
A: 确保使用xelatex作为PDF引擎，或者在Markdown文件开头添加适当的编码声明。

**Q: pdflatex命令未找到**
A: 确认TeX Live已正确安装，检查`which pdflatex`是否返回有效路径。

**Q: 字体显示不正确**
A: 安装额外的字体包：`sudo yum install google-droid-sans-fonts`

## 🤖 Moltbot集成

这个技能包专为Moltbot设计，可以通过以下方式调用：

- **直接调用脚本**: 在Moltbot会话中执行转换命令
- **自动化工作流**: 集成到n8n或其他自动化工具中
- **定时任务**: 通过cron定期转换文档

## 📄 许可证

MIT License - 免费使用和修改。

## 🙏 致谢

感谢以下开源项目：
- [Pandoc](https://pandoc.org/) - 通用文档转换器
- [TeX Live](https://www.tug.org/texlive/) - LaTeX发行版
- [Moltbot](https://molt.bot) - AI助手框架

---

> **提示**: 这个技能包会持续更新，添加更多格式转换功能。欢迎提交功能请求或改进建议！