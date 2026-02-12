# Format Converter Usage Examples

## Markdown to PDF Conversion

### Basic Usage
```bash
python scripts/md_to_pdf.py input.md output.pdf
```

### With Custom Styling
```bash
python scripts/md_to_pdf.py --css custom.css input.md output.pdf
```

### With LaTeX Template
```bash
python scripts/md_to_pdf.py --template custom.latex input.md output.pdf
```

## Supported Features
- Table of contents generation
- Section numbering
- Code syntax highlighting
- Custom CSS styling (for HTML-based conversion)
- Custom LaTeX templates
- Unicode support (use English text for best results with pdflatex)

## Limitations
- Chinese characters may not render properly with pdflatex engine
- For full Unicode support, consider using xelatex (requires additional setup)
- Complex Markdown features like footnotes are supported but may need template customization