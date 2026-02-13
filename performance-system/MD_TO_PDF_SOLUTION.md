# Markdown to PDF 转换解决方案

## 问题描述
原始的Markdown转PDF转换脚本（使用pandoc + LaTeX）在处理包含中文内容的Markdown文件时失败，出现LaTeX错误：
```
! Missing number, treated as zero.
<to be read again> 
                   \protect 
l.518 ...nter}\rule{0.5\linewidth}{\linethickness}
```

此外，即使成功生成PDF，也会出现中文乱码问题。

## 根本原因分析
1. **LaTeX兼容性问题**: pandoc生成的LaTeX代码在处理某些Markdown表格格式时与xelatex/pdflatex不兼容
2. **缺少中文字体**: 系统未安装中文字体，导致weasyprint等HTML-to-PDF引擎无法正确渲染中文

## 解决方案

### 1. 使用WeasyPrint替代方案
创建改进的转换脚本 `fix_md_to_pdf.py`，采用两步转换：
- 第一步：Markdown → HTML (使用pandoc)
- 第二步：HTML → PDF (使用weasyprint)

### 2. 安装中文字体支持
在Alibaba Cloud Linux系统中安装文泉驿微米黑字体：
```bash
sudo yum install -y wqy-microhei-fonts
sudo fc-cache -fv
```

### 3. 改进的转换脚本
脚本特点：
- 自动处理中文内容
- 支持表格和复杂格式
- 包含适当的CSS样式确保专业外观
- 错误处理和用户友好的输出

## 使用方法
```bash
# 基本转换
python3 fix_md_to_pdf.py input.md output.pdf

# 示例
python3 fix_md_to_pdf.py SDD.md SDD_fixed.pdf
```

## 依赖要求
- **pandoc**: Markdown到HTML转换
- **weasyprint**: HTML到PDF转换
- **wqy-microhei-fonts**: 中文字体支持
- **fontconfig**: 字体管理

## 安装依赖（Alibaba Cloud Linux）
```bash
# 安装pandoc和weasyprint
# (假设已通过其他方式安装)

# 安装中文字体
sudo yum install -y wqy-microhei-fonts
sudo fc-cache -fv
```

## 文件列表
- `fix_md_to_pdf.py`: 主转换脚本
- `SDD_fixed.pdf`: 成功转换的示例输出
- `MD_TO_PDF_SOLUTION.md`: 本解决方案文档

## 版本信息
- **创建日期**: 2026-02-13
- **作者**: 哈罗助手
- **适用系统**: Alibaba Cloud Linux / CentOS / RHEL

## 注意事项
- 确保系统已安装中文字体，否则仍会出现乱码
- weasyprint对复杂CSS支持有限，如需高级排版可考虑其他方案
- 此方案特别适合包含中文的技术文档转换