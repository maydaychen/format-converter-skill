#!/usr/bin/env python3
"""
Improved Markdown to PDF converter that handles Chinese content and tables properly.

This script converts Markdown files to PDF using weasyprint (HTML/CSS based)
which handles tables and Chinese characters better than LaTeX-based approaches.
"""

import argparse
import subprocess
import sys
import os
from pathlib import Path

def convert_md_to_pdf(input_file, output_file):
    """
    Convert Markdown file to PDF using weasyprint via HTML intermediate
    
    Args:
        input_file (str): Path to input Markdown file
        output_file (str): Path to output PDF file
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")
    
    # Ensure output directory exists
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create temporary HTML file path
    html_file = output_file.replace('.pdf', '.html')
    
    try:
        # Step 1: Convert Markdown to HTML with pandoc
        cmd1 = ['pandoc', input_file, '-o', html_file, '--standalone']
        result1 = subprocess.run(cmd1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, 
                                universal_newlines=True, check=True)
        
        # Step 2: Convert HTML to PDF with weasyprint
        cmd2 = ['weasyprint', html_file, output_file]
        result2 = subprocess.run(cmd2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, 
                                universal_newlines=True, check=True)
        
        print(f"Successfully converted {input_file} to {output_file}")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Error converting file: {e}")
        if hasattr(e, 'stderr') and e.stderr:
            print(f"stderr: {e.stderr}")
        return False
    except OSError as e:
        print(f"Error: {e}")
        return False
    finally:
        # Clean up temporary HTML file
        if os.path.exists(html_file):
            os.remove(html_file)

def main():
    parser = argparse.ArgumentParser(description='Convert Markdown to PDF (improved version)')
    parser.add_argument('input', help='Input markdown file')
    parser.add_argument('output', help='Output PDF file')
    
    args = parser.parse_args()
    
    success = convert_md_to_pdf(args.input, args.output)
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()