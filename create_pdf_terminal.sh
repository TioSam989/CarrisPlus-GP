#!/bin/bash
# Terminal-based PDF creator for CarrisPlus Documentation
# Works on Git Bash, WSL, Linux, macOS

echo "========================================="
echo "CarrisPlus - PDF Generator (Terminal)"
echo "========================================="
echo ""

# Check if we're in the right directory
if [ ! -f "DOCUMENTATION.md" ]; then
    echo "ERROR: DOCUMENTATION.md not found!"
    echo "Please run this script from the CarrisPlus-GP directory"
    exit 1
fi

echo "Converting DOCUMENTATION.md to HTML..."
python3 convert_to_html.py 2>/dev/null || python convert_to_html.py

if [ -f "CarrisPlus_Documentation.html" ]; then
    echo ""
    echo "✓ HTML created successfully!"
    echo ""
    echo "========================================="
    echo "NEXT STEPS TO CREATE PDF:"
    echo "========================================="
    echo ""
    echo "METHOD 1 - Using Browser (Easiest):"
    echo "  1. Open: CarrisPlus_Documentation.html"
    echo "  2. Press: Ctrl+P"
    echo "  3. Select: 'Save as PDF'"
    echo "  4. Click: Save"
    echo ""
    echo "METHOD 2 - Using wkhtmltopdf (If installed):"
    echo "  wkhtmltopdf CarrisPlus_Documentation.html CarrisPlus.pdf"
    echo ""
    echo "METHOD 3 - Using Chrome headless:"
    echo "  chrome --headless --print-to-pdf=CarrisPlus.pdf CarrisPlus_Documentation.html"
    echo ""
    echo "========================================="
    echo ""
    echo "Opening HTML in default browser..."

    # Try to open in browser based on OS
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        xdg-open CarrisPlus_Documentation.html 2>/dev/null || echo "Please open CarrisPlus_Documentation.html manually"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        open CarrisPlus_Documentation.html
    elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
        start CarrisPlus_Documentation.html
    fi
else
    echo "ERROR: Failed to create HTML file"
    exit 1
fi
