"""
Convert Modelacao_CarrisPlus.md to PDF
"""
from markdown2 import markdown
from weasyprint import HTML
from pathlib import Path

def convert_md_to_pdf(md_file, pdf_file):
    """Convert markdown file to PDF"""

    # Read markdown content
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert markdown to HTML
    html_content = markdown(md_content, extras=['tables', 'fenced-code-blocks', 'header-ids'])

    # Create styled HTML
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            @page {{
                size: A4;
                margin: 2cm;
                @bottom-center {{
                    content: counter(page) " / " counter(pages);
                }}
            }}
            body {{
                font-family: 'Arial', sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 800px;
                margin: 0 auto;
            }}
            h1 {{
                color: #2c3e50;
                border-bottom: 3px solid #3498db;
                padding-bottom: 10px;
                page-break-before: always;
            }}
            h1:first-of-type {{
                page-break-before: avoid;
            }}
            h2 {{
                color: #34495e;
                border-bottom: 2px solid #95a5a6;
                padding-bottom: 5px;
                margin-top: 30px;
            }}
            h3 {{
                color: #7f8c8d;
                margin-top: 20px;
            }}
            h4 {{
                color: #95a5a6;
                margin-top: 15px;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 20px 0;
                page-break-inside: avoid;
            }}
            th, td {{
                border: 1px solid #bdc3c7;
                padding: 12px;
                text-align: left;
            }}
            th {{
                background-color: #3498db;
                color: white;
                font-weight: bold;
            }}
            tr:nth-child(even) {{
                background-color: #ecf0f1;
            }}
            code {{
                background-color: #f8f9fa;
                padding: 2px 6px;
                border-radius: 3px;
                font-family: 'Courier New', monospace;
                font-size: 0.9em;
            }}
            pre {{
                background-color: #f8f9fa;
                padding: 15px;
                border-radius: 5px;
                border-left: 4px solid #3498db;
                overflow-x: auto;
                page-break-inside: avoid;
            }}
            ul, ol {{
                margin-left: 20px;
            }}
            li {{
                margin-bottom: 8px;
            }}
            strong {{
                color: #2c3e50;
            }}
            hr {{
                border: none;
                border-top: 2px solid #bdc3c7;
                margin: 30px 0;
            }}
            .page-break {{
                page-break-after: always;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Convert HTML to PDF
    HTML(string=styled_html).write_pdf(pdf_file)
    print(f"PDF created successfully: {pdf_file}")

if __name__ == "__main__":
    md_file = Path(__file__).parent / "Modelacao_CarrisPlus.md"
    pdf_file = Path(__file__).parent / "Modelacao_CarrisPlus.pdf"

    convert_md_to_pdf(md_file, pdf_file)
