#!/usr/bin/env python3
"""
Terminal-based PDF creator for CarrisPlus
Works on any system with Python
No external dependencies required for HTML generation
"""

import sys
import os
import subprocess
from pathlib import Path

def check_tools():
    """Check available PDF conversion tools"""
    tools = {}

    # Check for wkhtmltopdf
    try:
        subprocess.run(['wkhtmltopdf', '--version'],
                      stdout=subprocess.DEVNULL,
                      stderr=subprocess.DEVNULL)
        tools['wkhtmltopdf'] = True
    except:
        tools['wkhtmltopdf'] = False

    # Check for Chrome/Chromium
    chrome_paths = [
        'google-chrome',
        'chrome',
        'chromium',
        'chromium-browser',
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
        'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
    ]

    tools['chrome'] = False
    for chrome in chrome_paths:
        try:
            subprocess.run([chrome, '--version'],
                          stdout=subprocess.DEVNULL,
                          stderr=subprocess.DEVNULL)
            tools['chrome'] = chrome
            break
        except:
            continue

    return tools

def create_html():
    """Generate HTML file from markdown"""
    print("Converting DOCUMENTATION.md to HTML...")
    try:
        subprocess.run([sys.executable, 'convert_to_html.py'], check=True)
        return True
    except:
        print("ERROR: Failed to create HTML")
        return False

def convert_with_wkhtmltopdf():
    """Convert HTML to PDF using wkhtmltopdf"""
    print("\nConverting HTML to PDF using wkhtmltopdf...")
    try:
        subprocess.run([
            'wkhtmltopdf',
            '--enable-local-file-access',
            '--page-size', 'A4',
            '--margin-top', '20mm',
            '--margin-bottom', '20mm',
            '--margin-left', '20mm',
            '--margin-right', '20mm',
            'CarrisPlus_Documentation.html',
            'CarrisPlus_Documentation.pdf'
        ], check=True)
        return True
    except Exception as e:
        print(f"ERROR: {e}")
        return False

def convert_with_chrome(chrome_path):
    """Convert HTML to PDF using Chrome headless"""
    print(f"\nConverting HTML to PDF using Chrome...")

    html_path = Path('CarrisPlus_Documentation.html').absolute()
    pdf_path = Path('CarrisPlus_Documentation.pdf').absolute()

    try:
        subprocess.run([
            chrome_path,
            '--headless',
            '--disable-gpu',
            f'--print-to-pdf={pdf_path}',
            f'file:///{html_path}'
        ], check=True)
        return True
    except Exception as e:
        print(f"ERROR: {e}")
        return False

def main():
    print("=" * 50)
    print("CarrisPlus - PDF Generator (Terminal)")
    print("=" * 50)
    print()

    # Check if we're in the right directory
    if not Path('DOCUMENTATION.md').exists():
        print("ERROR: DOCUMENTATION.md not found!")
        print("Please run this script from the CarrisPlus-GP directory")
        sys.exit(1)

    # Create HTML first
    if not create_html():
        sys.exit(1)

    if not Path('CarrisPlus_Documentation.html').exists():
        print("ERROR: HTML file was not created")
        sys.exit(1)

    print("\n[OK] HTML created successfully!")

    # Check available tools
    print("\nChecking for PDF conversion tools...")
    tools = check_tools()

    # Try automatic conversion
    converted = False

    if tools['wkhtmltopdf']:
        print("\n[FOUND] wkhtmltopdf")
        if convert_with_wkhtmltopdf():
            converted = True

    if not converted and tools['chrome']:
        print("\n[FOUND] Chrome/Chromium")
        if convert_with_chrome(tools['chrome']):
            converted = True

    # Show results
    print("\n" + "=" * 50)

    if converted:
        pdf_size = Path('CarrisPlus_Documentation.pdf').stat().st_size / 1024
        print("[SUCCESS] PDF created successfully!")
        print(f"\nFile: CarrisPlus_Documentation.pdf")
        print(f"Size: {pdf_size:.2f} KB")
    else:
        print("[INFO] Automatic PDF conversion not available")
        print("\nMANUAL STEPS TO CREATE PDF:")
        print("=" * 50)
        print("\n1. Open CarrisPlus_Documentation.html in your browser")
        print("2. Press Ctrl+P (or Cmd+P on Mac)")
        print("3. Select 'Save as PDF'")
        print("4. Click Save")
        print("\nOr install a PDF conversion tool:")
        print("  - wkhtmltopdf: sudo apt install wkhtmltopdf")
        print("  - Or use Google Chrome")

    print("\n" + "=" * 50)

if __name__ == '__main__':
    main()
