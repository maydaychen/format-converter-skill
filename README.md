# Format Converter Skill

A comprehensive file format conversion toolkit for Moltbot that supports converting between common document formats with professional quality output.

## 🚀 Features

- **Markdown to PDF**: High-quality PDF generation with proper typography, table of contents, and code highlighting
- **Multi-language Support**: Full Unicode support including Chinese, Japanese, and other international characters
- **Custom Styling**: Apply custom CSS styles or LaTeX templates for branded output
- **Professional Layout**: Automatic section numbering, headers, footers, and page formatting
- **Extensible Design**: Easy to add new format converters (HTML, DOCX, CSV, etc.)

## 📁 Directory Structure

```
format-converter/
├── SKILL.md                 # Skill metadata and usage instructions
├── README.md               # This file
├── scripts/                # Executable conversion scripts
│   └── md_to_pdf.py       # Markdown to PDF converter
└── references/             # Documentation and examples
    └── usage_examples.md   # Practical usage examples
```

## ⚙️ Installation Requirements

The skill requires the following system dependencies:

- **pandoc** (v2.0+) - Universal document converter
- **TeX Live** - LaTeX typesetting system
  - Basic collection (`texlive-collection-basic`)
  - Font recommendations (`texlive-collection-fontsrecommended`)  
  - LaTeX collection (`texlive-collection-latex`)

These are automatically installed when the skill is deployed on compatible systems.

## 🎯 Usage

### Basic Markdown to PDF Conversion

```bash
python3 scripts/md_to_pdf.py input.md output.pdf
```

### Advanced Options

```bash
# With custom CSS styling
python3 scripts/md_to_pdf.py --css styles.css input.md output.pdf

# With custom LaTeX template
python3 scripts/md_to_pdf.py --template template.latex input.md output.pdf
```

### Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `input` | Input Markdown file path | Required |
| `output` | Output PDF file path | Required |
| `--css` | Path to CSS file for styling | None |
| `--template` | Path to LaTeX template file | None |

## 🌟 Example Workflow

1. **Create your Markdown document** (`document.md`)
2. **(Optional) Create custom styling** (`styles.css`)
3. **Run the converter**:
   ```bash
   python3 scripts/md_to_pdf.py document.md document.pdf
   ```
4. **Get professional PDF output** ready for sharing or printing

## 🔧 Technical Details

- **Engine**: Uses pandoc with pdflatex/xelatex backend
- **Unicode Support**: Full UTF-8 support with proper font handling
- **Error Handling**: Comprehensive error messages and exit codes
- **Compatibility**: Works with Python 3.6+ and standard Unix/Linux systems

## 📈 Future Extensions

Planned format conversions to add:
- HTML ↔ Markdown bidirectional conversion
- DOCX ↔ Markdown conversion  
- CSV ↔ JSON data format conversion
- Image format conversions (PNG, JPEG, WebP)
- EPUB ebook generation

## 🤝 Integration with Moltbot

This skill integrates seamlessly with Moltbot's agent system:
- Automatically triggered when format conversion is needed
- Provides clear usage instructions in `SKILL.md`
- Bundled resources are loaded only when needed to minimize context usage
- Follows Moltbot's progressive disclosure design principles

## 📄 License

This skill is designed for use with Moltbot and follows the same licensing terms as the Moltbot platform.

---

**Note**: For Chinese and other CJK language support, ensure xelatex is available and consider using appropriate LaTeX templates with CJK font packages.