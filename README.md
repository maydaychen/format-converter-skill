# Format Converter Skill

A Moltbot skill for common format conversions, starting with Markdown to PDF.

## Features

- **Markdown to PDF**: Convert Markdown files to high-quality PDF documents
- **Chinese Support**: Full Unicode and Chinese character support via XeLaTeX
- **Custom Styling**: Support for CSS stylesheets and LaTeX templates
- **Professional Typesetting**: Automatic table of contents, section numbering, code highlighting
- **Multiple PDF Engines**: Support for both pdflatex (English) and xelatex (Unicode/Chinese)

## Requirements

- Python 3.6+
- Pandoc >= 2.0
- TeX Live (basic + fonts recommended collections)
- Required Python packages: none (uses only standard library)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/maydaychen/format-converter-skill.git
   ```

2. Install dependencies:
   ```bash
   # Install pandoc
   sudo apt-get install pandoc  # Ubuntu/Debian
   sudo yum install pandoc      # CentOS/RHEL
   
   # Install TeX Live (minimum required)
   sudo apt-get install texlive texlive-xetex texlive-fonts-recommended
   ```

## Usage

### Basic Conversion
```bash
python3 scripts/md_to_pdf.py input.md output.pdf
```

### With Custom CSS
```bash
python3 scripts/md_to_pdf.py --css style.css input.md output.pdf
```

### With LaTeX Template
```bash
python3 scripts/md_to_pdf.py --template template.latex input.md output.pdf
```

### Specify PDF Engine (for advanced use)
The script automatically detects if the input contains Unicode characters and uses xelatex accordingly.
For manual control, you can modify the script or use pandoc directly:

```bash
# For English-only documents (faster)
pandoc input.md -o output.pdf --pdf-engine=pdflatex

# For Unicode/Chinese documents
pandoc input.md -o output.pdf --pdf-engine=xelatex
```

## Examples

### Simple Document
```bash
python3 scripts/md_to_pdf.py examples/simple.md simple.pdf
```

### Document with Chinese
```bash
python3 scripts/md_to_pdf.py examples/chinese.md chinese.pdf
```

### Document with Custom Styling
```bash
python3 scripts/md_to_pdf.py --css examples/style.css styled.md styled.pdf
```

## Error Handling

Common errors and solutions:

- **"pdflatex not found"**: Install TeX Live basic packages
- **"Unicode character not set up for use with LaTeX"**: The script should automatically switch to xelatex, but if it doesn't, ensure your document encoding is UTF-8
- **"Permission denied"**: Ensure output directory is writable
- **Table formatting issues**: Avoid complex table structures or use HTML tables instead of Markdown tables

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