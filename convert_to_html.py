"""
Convert Markdown to HTML - Then open in browser and Print to PDF
This is the EASIEST method - no special libraries needed!
"""

def convert_md_to_html():
    """Convert DOCUMENTATION.md to a beautiful HTML file"""

    # Read markdown content
    with open('DOCUMENTATION.md', 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Simple markdown to HTML conversion
    # Replace headers
    html_content = md_content

    # Convert headers
    html_content = html_content.replace('\n# ', '\n<h1>')
    html_content = html_content.replace('\n## ', '\n<h2>')
    html_content = html_content.replace('\n### ', '\n<h3>')
    html_content = html_content.replace('\n#### ', '\n<h4>')

    # Close header tags (simple approach)
    lines = html_content.split('\n')
    processed_lines = []

    for line in lines:
        if line.startswith('<h1>'):
            line = line.replace('<h1>', '<h1>') + '</h1>'
        elif line.startswith('<h2>'):
            line = line.replace('<h2>', '<h2>') + '</h2>'
        elif line.startswith('<h3>'):
            line = line.replace('<h3>', '<h3>') + '</h3>'
        elif line.startswith('<h4>'):
            line = line.replace('<h4>', '<h4>') + '</h4>'

        # Convert bold
        if '**' in line:
            parts = line.split('**')
            new_line = ''
            for i, part in enumerate(parts):
                if i % 2 == 1:
                    new_line += f'<strong>{part}</strong>'
                else:
                    new_line += part
            line = new_line

        # Convert code blocks
        if line.startswith('```'):
            if '<pre><code>' not in ''.join(processed_lines[-5:]):
                line = '<pre><code>'
            else:
                line = '</code></pre>'

        processed_lines.append(line)

    html_body = '\n'.join(processed_lines)

    # Create full HTML with styling
    html_template = f"""<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CarrisPlus - Documentação Técnica</title>
    <style>
        @media print {{
            @page {{
                size: A4;
                margin: 2cm;
            }}

            h1 {{
                page-break-before: always;
            }}

            h1:first-of-type {{
                page-break-before: avoid;
            }}

            table {{
                page-break-inside: avoid;
            }}
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.8;
            color: #333;
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 20px;
            background-color: #fff;
        }}

        /* Cover page */
        .cover {{
            text-align: center;
            padding: 100px 0;
            page-break-after: always;
        }}

        .cover h1 {{
            font-size: 3em;
            color: #2c3e50;
            margin-bottom: 20px;
            border: none;
        }}

        .cover .subtitle {{
            font-size: 1.5em;
            color: #7f8c8d;
            margin-bottom: 40px;
        }}

        .cover .team {{
            margin-top: 80px;
            font-size: 1.1em;
        }}

        /* Headers */
        h1 {{
            color: #2c3e50;
            border-bottom: 4px solid #3498db;
            padding-bottom: 15px;
            margin-top: 60px;
            margin-bottom: 30px;
            font-size: 2.2em;
        }}

        h2 {{
            color: #2980b9;
            border-bottom: 2px solid #bdc3c7;
            padding-bottom: 10px;
            margin-top: 40px;
            margin-bottom: 20px;
            font-size: 1.8em;
        }}

        h3 {{
            color: #34495e;
            margin-top: 30px;
            margin-bottom: 15px;
            font-size: 1.4em;
        }}

        h4 {{
            color: #555;
            margin-top: 20px;
            margin-bottom: 10px;
            font-size: 1.2em;
        }}

        /* Paragraphs */
        p {{
            margin: 15px 0;
            text-align: justify;
        }}

        /* Lists */
        ul, ol {{
            margin: 20px 0;
            padding-left: 40px;
        }}

        li {{
            margin: 10px 0;
            line-height: 1.6;
        }}

        /* Tables */
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 30px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}

        th {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
            border: none;
        }}

        td {{
            padding: 12px 15px;
            border: 1px solid #e0e0e0;
        }}

        tr:nth-child(even) {{
            background-color: #f8f9fa;
        }}

        tr:hover {{
            background-color: #e3f2fd;
        }}

        /* Code blocks */
        code {{
            background-color: #f4f4f4;
            padding: 3px 8px;
            border-radius: 4px;
            font-family: 'Courier New', Consolas, monospace;
            font-size: 0.9em;
            color: #e74c3c;
        }}

        pre {{
            background-color: #2c3e50;
            color: #ecf0f1;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
            margin: 25px 0;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}

        pre code {{
            background-color: transparent;
            padding: 0;
            color: #ecf0f1;
            font-size: 0.95em;
        }}

        /* Blockquotes */
        blockquote {{
            border-left: 5px solid #3498db;
            padding-left: 20px;
            margin: 25px 0;
            font-style: italic;
            color: #555;
            background-color: #ecf8ff;
            padding: 15px 20px;
            border-radius: 0 5px 5px 0;
        }}

        /* Strong text */
        strong {{
            color: #2c3e50;
            font-weight: 600;
        }}

        /* Horizontal rules */
        hr {{
            border: none;
            border-top: 3px solid #ecf0f1;
            margin: 50px 0;
        }}

        /* Status badges */
        .status {{
            display: inline-block;
            padding: 4px 10px;
            border-radius: 12px;
            font-size: 0.85em;
            font-weight: 600;
        }}

        .status-complete {{
            background-color: #d4edda;
            color: #155724;
        }}

        .status-pending {{
            background-color: #fff3cd;
            color: #856404;
        }}

        .status-blocked {{
            background-color: #f8d7da;
            color: #721c24;
        }}

        /* Print button */
        .print-button {{
            position: fixed;
            top: 20px;
            right: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 50px;
            font-size: 1em;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
            z-index: 1000;
            transition: all 0.3s ease;
        }}

        .print-button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
        }}

        @media print {{
            .print-button {{
                display: none;
            }}
        }}

        /* Emoji and icons */
        .emoji {{
            font-size: 1.2em;
        }}
    </style>
</head>
<body>
    <button class="print-button" onclick="window.print()">🖨️ Imprimir / Salvar PDF</button>

    <div class="cover">
        <h1>🚌 CarrisPlus</h1>
        <div class="subtitle">Sistema de Gestão de Documentos Online</div>
        <div class="subtitle" style="font-size: 1.2em;">Documentação Técnica Completa</div>

        <div class="team">
            <p><strong>Equipa de Desenvolvimento:</strong></p>
            <p>Davi (2024301) • Iago (2024195) • Ana (2024184)</p>
        </div>

        <div style="margin-top: 80px; color: #7f8c8d;">
            <p>Projeto Académico - Engenharia Informática</p>
            <p>Ano Letivo 2024/2025</p>
        </div>
    </div>

    {html_body}

</body>
</html>
"""

    # Write HTML file
    with open('CarrisPlus_Documentation.html', 'w', encoding='utf-8') as f:
        f.write(html_template)

    print("[OK] HTML file created: CarrisPlus_Documentation.html")
    print("\nHOW TO CREATE PDF:")
    print("1. Open 'CarrisPlus_Documentation.html' in your web browser")
    print("2. Press Ctrl+P (or click the Print button)")
    print("3. Select 'Save as PDF' as the printer")
    print("4. Click 'Save'")
    print("\nThe HTML file looks beautiful and converts perfectly to PDF!")

if __name__ == '__main__':
    convert_md_to_html()
