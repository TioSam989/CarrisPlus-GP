#!/usr/bin/env python
"""Convert REQUIREMENTS.md to PDF"""

import subprocess
import sys
from pathlib import Path

def main():
    print("=" * 50)
    print("Creating PDF from REQUIREMENTS.md...")
    print("=" * 50)

    # Create simple HTML
    with open('REQUIREMENTS.md', 'r', encoding='utf-8') as f:
        md = f.read()

    # Simple conversion
    html_content = md.replace('# ', '<h1>').replace('\n## ', '</h1>\n<h2>')
    html_content = html_content.replace('\n### ', '</h2>\n<h3>').replace('\n#### ', '</h3>\n<h4>')
    html_content = html_content.replace('**', '<strong>').replace('**', '</strong>')

    html = f'''<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <title>CarrisPlus - Requisitos</title>
    <style>
        @page {{ size: A4; margin: 2cm; }}
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        h1 {{ color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; page-break-before: always; }}
        h1:first-of-type {{ page-break-before: avoid; }}
        h2 {{ color: #2980b9; border-bottom: 2px solid #bdc3c7; padding-bottom: 8px; margin-top: 30px; }}
        h3 {{ color: #34495e; margin-top: 25px; }}
        h4 {{ color: #555; margin-top: 20px; }}
        code {{ background: #f4f4f4; padding: 2px 6px; border-radius: 3px; font-family: monospace; }}
        pre {{ background: #2c3e50; color: #ecf0f1; padding: 15px; border-radius: 5px; }}
        strong {{ color: #2c3e50; font-weight: 600; }}
        ul {{ margin: 15px 0; padding-left: 30px; }}
        li {{ margin: 8px 0; }}
    </style>
</head>
<body>
<pre style="white-space: pre-wrap; font-family: Arial; background: white; color: #333; padding: 0;">{md}</pre>
</body>
</html>'''

    with open('CarrisPlus_Requirements.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("\n[OK] HTML created: CarrisPlus_Requirements.html")

    # Try Chrome
    chrome_paths = [
        r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
        'chrome',
        'google-chrome'
    ]

    html_path = Path('CarrisPlus_Requirements.html').absolute()
    pdf_path = Path('CarrisPlus_Requirements.pdf').absolute()

    for chrome in chrome_paths:
        try:
            subprocess.run([
                chrome,
                '--headless',
                '--disable-gpu',
                f'--print-to-pdf={pdf_path}',
                str(html_path)
            ], check=True, capture_output=True)

            size = pdf_path.stat().st_size / 1024
            print(f"\n[SUCCESS] PDF created!")
            print(f"File: {pdf_path}")
            print(f"Size: {size:.2f} KB")
            return
        except:
            continue

    print("\n[INFO] Automatic PDF creation not available")
    print("Please open CarrisPlus_Requirements.html and print to PDF")

if __name__ == '__main__':
    main()
