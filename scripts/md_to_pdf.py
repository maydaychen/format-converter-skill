#!/usr/bin/env python3
"""
Markdown to PDF converter using pandoc

This script converts Markdown files to PDF using pandoc with LaTeX backend.
It supports basic styling through CSS or custom LaTeX templates.

Usage:
    python md_to_pdf.py input.md output.pdf [--css style.css] [--template template.latex]
"""

import argparse
import subprocess
import sys
import os
from pathlib import Path

def convert_md_to_pdf(input_file, output_file, css_file=None, template_file=None):
    """
    Convert Markdown file to PDF using pandoc
    
    Args:
        input_file (str): Path to input Markdown file
        output_file (str): Path to output PDF file
        css_file (str, optional): Path to CSS file for styling (for HTML-based conversion)
        template_file (str, optional): Path to LaTeX template file
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError("Input file not found: {}".format(input_file))
    
    # Ensure output directory exists
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Build pandoc command
    cmd = ['pandoc', input_file, '-o', output_file]
    
    # Add PDF engine
    cmd.extend(['--pdf-engine=pdflatex'])
    
    # Add CSS if provided (for HTML-based styling)
    if css_file and os.path.exists(css_file):
        cmd.extend(['--css', css_file])
    
    # Add template if provided
    if template_file and os.path.exists(template_file):
        cmd.extend(['--template', template_file])
    
    # Add default extensions for better Markdown support
    cmd.extend([
        '--standalone',
        '--toc',  # Table of contents
        '--number-sections',  # Number sections
        '--highlight-style=pygments'  # Code highlighting
    ])
    
    try:
        # Use universal_newlines instead of text for Python 3.6 compatibility
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)
        print("Successfully converted {} to {}".format(input_file, output_file))
        return True
    except subprocess.CalledProcessError as e:
        print("Error converting file: {}".format(e))
        print("stderr: {}".format(e.stderr))
        return False
    except OSError as e:
        print("Error: {}".format(e))
        return False

def main():
    parser = argparse.ArgumentParser(description='Convert Markdown to PDF')
    parser.add_argument('input', help='Input markdown file')
    parser.add_argument('output', help='Output PDF file')
    parser.add_argument('--css', help='Optional CSS file for styling')
    parser.add_argument('--template', help='Optional LaTeX template file')
    
    args = parser.parse_args()
    
    success = convert_md_to_pdf(
        args.input, 
        args.output, 
        args.css, 
        args.template
    )
    
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()