#!/usr/bin/env python3
"""
Markdown to PDF converter using pandoc with xelatex (for Chinese support)

This script converts Markdown files to PDF using pandoc with xelatex engine.
It's specifically designed for documents containing Chinese characters.

Usage:
    python md_to_pdf_xe.py input.md output.pdf [--css style.css] [--template template.latex]
"""

import argparse
import subprocess
import sys
import os

def convert_md_to_pdf(input_file, output_file, css_file=None, template_file=None):
    """
    Convert Markdown file to PDF using pandoc with xelatex
    
    Args:
        input_file (str): Path to input Markdown file
        output_file (str): Path to output PDF file
        css_file (str, optional): Path to CSS file for styling
        template_file (str, optional): Path to LaTeX template file
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError("Input file not found: {}".format(input_file))
    
    # Ensure output directory exists
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Build pandoc command with xelatex
    cmd = ['pandoc', input_file, '-o', output_file]
    
    # Use xelatex for Chinese support
    cmd.extend(['--pdf-engine=xelatex'])
    
    # Add CSS if provided
    if css_file and os.path.exists(css_file):
        cmd.extend(['--css', css_file])
    
    # Add template if provided
    if template_file and os.path.exists(template_file):
        cmd.extend(['--template', template_file])
    
    # Add default extensions
    cmd.extend([
        '--standalone',
        '--toc',
        '--number-sections',
        '--highlight-style=pygments'
    ])
    
    try:
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
    parser = argparse.ArgumentParser(description='Convert Markdown to PDF (with Chinese support)')
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