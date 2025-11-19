"""
Simple Markdown to PDF converter for CarrisPlus Documentation
No external dependencies needed - uses built-in libraries
"""

import markdown
from weasyprint import HTML
from pathlib import Path

def convert_markdown_to_pdf():
    """Convert DOCUMENTATION.md to PDF"""

    # Read the markdown file
    md_file = Path('DOCUMENTATION.md')
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert markdown to HTML
    html_content = markdown.markdown(
        md_content,
        extensions=['tables', 'fenced_code', 'codehilite', 'toc']
    )

    # Add CSS styling
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            @page {{
                size: A4;
                margin: 2.5cm;
                @bottom-center {{
                    content: "Página " counter(page) " de " counter(pages);
                }}
            }}

            body {{
                font-family: Arial, Helvetica, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 100%;
            }}

            h1 {{
                color: #2c3e50;
                border-bottom: 3px solid #3498db;
                padding-bottom: 10px;
                page-break-before: always;
                margin-top: 0;
            }}

            h1:first-of-type {{
                page-break-before: avoid;
            }}

            h2 {{
                color: #2980b9;
                border-bottom: 2px solid #bdc3c7;
                padding-bottom: 5px;
                margin-top: 30px;
            }}

            h3 {{
                color: #34495e;
                margin-top: 20px;
            }}

            h4 {{
                color: #7f8c8d;
            }}

            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 20px 0;
                font-size: 0.9em;
            }}

            th {{
                background-color: #3498db;
                color: white;
                padding: 12px;
                text-align: left;
                font-weight: bold;
            }}

            td {{
                padding: 10px;
                border: 1px solid #ddd;
            }}

            tr:nth-child(even) {{
                background-color: #f8f9fa;
            }}

            code {{
                background-color: #f4f4f4;
                padding: 2px 6px;
                border-radius: 3px;
                font-family: 'Courier New', monospace;
                font-size: 0.9em;
            }}

            pre {{
                background-color: #2c3e50;
                color: #ecf0f1;
                padding: 15px;
                border-radius: 5px;
                overflow-x: auto;
                font-size: 0.85em;
                line-height: 1.4;
            }}

            pre code {{
                background-color: transparent;
                padding: 0;
                color: #ecf0f1;
            }}

            blockquote {{
                border-left: 4px solid #3498db;
                padding-left: 20px;
                margin-left: 0;
                font-style: italic;
                color: #555;
            }}

            ul, ol {{
                margin: 15px 0;
                padding-left: 30px;
            }}

            li {{
                margin: 8px 0;
            }}

            .page-break {{
                page-break-after: always;
            }}

            strong {{
                color: #2c3e50;
            }}

            hr {{
                border: none;
                border-top: 2px solid #bdc3c7;
                margin: 30px 0;
            }}

            /* Cover page styling */
            .cover {{
                text-align: center;
                padding-top: 100px;
                page-break-after: always;
            }}

            .cover h1 {{
                font-size: 2.5em;
                border: none;
                color: #2c3e50;
            }}

            .cover h2 {{
                color: #7f8c8d;
                border: none;
                font-weight: normal;
            }}
        </style>
    </head>
    <body>
        <div class="cover">
            <h1>CarrisPlus</h1>
            <h2>Sistema de Gestão de Documentos Online</h2>
            <h3>Documentação Técnica Completa</h3>
            <p style="margin-top: 100px;">
                <strong>Equipa de Desenvolvimento:</strong><br>
                Davi (2024301) | Iago (2024195) | Ana (2024184)
            </p>
            <p style="margin-top: 50px;">
                Projeto Académico - Engenharia Informática<br>
                Ano Letivo 2024/2025
            </p>
        </div>

        {html_content}
    </body>
    </html>
    """

    # Convert HTML to PDF
    output_file = Path('CarrisPlus_Documentation.pdf')
    HTML(string=styled_html).write_pdf(output_file)

    print(f"✅ PDF created successfully: {output_file}")
    print(f"📄 File size: {output_file.stat().st_size / 1024:.2f} KB")

if __name__ == '__main__':
    try:
        convert_markdown_to_pdf()
    except ImportError as e:
        print("❌ Missing required libraries. Please install them:")
        print("\n  pip install markdown weasyprint\n")
        print("If weasyprint fails to install, try:")
        print("  pip install markdown reportlab md2pdf")
    except Exception as e:
        print(f"❌ Error: {e}")
