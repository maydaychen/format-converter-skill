# Format Converter Skill

A Moltbot skill for common format conversions, starting with Markdown to PDF.

## Features

- **Markdown to PDF**: Convert Markdown files to high-quality PDF documents
- **Chinese Support**: Full Unicode and Chinese character support via XeLaTeX or WeasyPrint
- **Custom Styling**: Support for CSS stylesheets and LaTeX templates
- **Professional Typesetting**: Automatic table of contents, section numbering, code highlighting
- **Multiple PDF Engines**: 
  - **LaTeX-based**: pdflatex (English) and xelatex (Unicode/Chinese)
  - **HTML-based**: WeasyPrint (better table and Chinese support)

## Requirements

### Option 1: LaTeX-based (default)
- Python 3.6+
- Pandoc >= 2.0
- TeX Live (basic + fonts recommended collections)

### Option 2: HTML-based (WeasyPrint)
- Python 3.6+
- Pandoc >= 2.0
- WeasyPrint (`pip install weasyprint`)
- System fonts (including Chinese fonts for Chinese content)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/maydaychen/format-converter-skill.git
   ```

2. Install dependencies:

   **For LaTeX-based conversion (recommended for most cases):**
   ```bash
   # Install pandoc
   sudo apt-get install pandoc  # Ubuntu/Debian
   sudo yum install pandoc      # CentOS/RHEL
   
   # Install TeX Live (minimum required)
   sudo apt-get install texlive texlive-xetex texlive-fonts-recommended
   ```

   **For HTML-based conversion (better for complex tables/Chinese):**
   ```bash
   pip install weasyprint
   # Also ensure system has Chinese fonts installed
   ```

## Usage

### LaTeX-based Conversion (default)
```bash
python3 scripts/md_to_pdf.py input.md output.pdf
```

### HTML-based Conversion (better Chinese/table support)
```bash
python3 scripts/md_to_pdf_weasyprint.py input.md output.pdf
```

### With Custom CSS (LaTeX-based)
```bash
python3 scripts/md_to_pdf.py --css style.css input.md output.pdf
```

### With LaTeX Template
```bash
python3 scripts/md_to_pdf.py --template template.latex input.md output.pdf
```

## Examples

### Simple Document (LaTeX)
```bash
python3 scripts/md_to_pdf.py examples/simple.md simple.pdf
```

### Document with Chinese (LaTeX)
```bash
python3 scripts/md_to_pdf.py examples/chinese.md chinese.pdf
```

### Document with Complex Tables (HTML/WeasyPrint)
```bash
python3 scripts/md_to_pdf_weasyprint.py examples/complex-tables.md tables.pdf
```

## Error Handling

Common errors and solutions:

- **"pdflatex not found"**: Install TeX Live basic packages
- **"Unicode character not set up for use with LaTeX"**: Use the WeasyPrint version or ensure proper encoding
- **"Permission denied"**: Ensure output directory is writable
- **Table formatting issues**: For complex tables, use the WeasyPrint version which handles HTML tables better

## Scripts

### `scripts/md_to_pdf.py`
- Uses pandoc + LaTeX (pdflatex/xelatex)
- Best for standard documents with good typography
- Requires TeX Live installation

### `scripts/md_to_pdf_xe.py`
- Uses pandoc + xelatex specifically for Chinese/Unicode
- Better Unicode support than pdflatex

### `scripts/md_to_pdf_weasyprint.py`
- Uses pandoc + WeasyPrint (HTML/CSS based)
- Better handling of complex tables and Chinese characters
- Doesn't require TeX Live, but needs WeasyPrint and system fonts

## Extending the Skill

To add new format conversions:

1. Create new scripts in the `scripts/` directory
2. Update `SKILL.md` description to include new capabilities
3. Add usage examples to `references/usage_examples.md`

Example script structure:
```python
def convert_format(input_file, output_file, **options):
    # Your conversion logic here
    pass
```

## License

MIT License - see LICENSE file for details.

## Author

Created by Haro Assistant for Moltbot.