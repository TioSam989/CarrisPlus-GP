@echo off
echo ====================================
echo CarrisPlus - PDF Generator
echo ====================================
echo.

python convert_to_html.py

echo.
echo Opening HTML in your default browser...
start CarrisPlus_Documentation.html

echo.
echo ====================================
echo NEXT STEPS:
echo 1. The HTML file should now be open in your browser
echo 2. Press Ctrl+P to print
echo 3. Select "Save as PDF" or "Microsoft Print to PDF"
echo 4. Choose where to save and click Save
echo ====================================
echo.
pause
