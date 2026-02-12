---
name: format-converter
description: Comprehensive file format conversion toolkit supporting Markdown to PDF, HTML, DOCX and other common formats. Use when Codex needs to convert between different document formats, especially for generating professional PDFs from Markdown files with proper styling and layout.
---

# Format Converter Skill

This skill provides tools for converting between various document formats, with a focus on high-quality output and professional presentation.

## Supported Conversions

- **Markdown → PDF**: Professional PDF generation with LaTeX backend
- **Markdown → HTML**: Web-ready HTML output  
- **Markdown → DOCX**: Microsoft Word compatible documents
- **Other formats**: Additional converters can be added as needed

## Quick Start

### Convert Markdown to PDF

```bash
# Basic conversion
python3 scripts/md_to_pdf.py input.md output.pdf

# With custom CSS styling
python3 scripts/md_to_pdf.py input.md output.pdf --css style.css
```

### Usage Examples

- "Convert my README.md to a professional PDF"
- "Generate a PDF report from this markdown document" 
- "Create a styled PDF from my documentation"

## Scripts

### `scripts/md_to_pdf.py`

Converts Markdown files to PDF using pandoc with LaTeX backend.

**Arguments:**
- `input`: Input markdown file path
- `output`: Output PDF file path  
- `--css`: Optional CSS file for styling (HTML-based)
- `--template`: Optional LaTeX template file

**Requirements:**
- pandoc (installed via system package manager)
- texlive (basic LaTeX distribution)

**Features:**
- Table of contents generation
- Section numbering
- Syntax highlighting for code blocks
- Professional typography and layout

## Adding New Converters

To add support for additional format conversions:

1. Create new scripts in the `scripts/` directory following the existing pattern
2. Update this SKILL.md file to document the new functionality
3. Ensure all dependencies are properly documented

## Best Practices

- Always validate input files exist before conversion
- Create output directories if they don't exist
- Use appropriate error handling for missing dependencies
- Provide clear feedback on conversion success/failure

## Dependencies

The skill requires the following system packages:
- `pandoc` - Document converter
- `texlive-collection-basic` - Basic LaTeX support
- `texlive-collection-fontsrecommended` - Recommended fonts
- `texlive-collection-latex` - Core LaTeX packages