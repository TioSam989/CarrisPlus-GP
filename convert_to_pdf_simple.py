"""
Simple Markdown to PDF converter using reportlab
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from pathlib import Path
import re

def parse_markdown_to_pdf(md_file, pdf_file):
    """Convert markdown to PDF using reportlab"""

    # Read markdown content
    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Create PDF
    doc = SimpleDocTemplate(
        str(pdf_file),
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )

    # Define styles
    styles = getSampleStyleSheet()

    # Custom styles - Professional black text only
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=22,
        textColor=colors.black,
        spaceAfter=24,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    h1_style = ParagraphStyle(
        'CustomH1',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=colors.black,
        spaceAfter=10,
        spaceBefore=16,
        fontName='Helvetica-Bold'
    )

    h2_style = ParagraphStyle(
        'CustomH2',
        parent=styles['Heading2'],
        fontSize=13,
        textColor=colors.black,
        spaceAfter=8,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )

    h3_style = ParagraphStyle(
        'CustomH3',
        parent=styles['Heading3'],
        fontSize=11,
        textColor=colors.black,
        spaceAfter=6,
        spaceBefore=10,
        fontName='Helvetica-Bold'
    )

    h4_style = ParagraphStyle(
        'CustomH4',
        parent=styles['Heading4'],
        fontSize=10,
        textColor=colors.black,
        spaceAfter=4,
        spaceBefore=8,
        fontName='Helvetica-Bold'
    )

    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=4,
        fontName='Helvetica',
        textColor=colors.black
    )

    code_style = ParagraphStyle(
        'CustomCode',
        parent=styles['Code'],
        fontSize=9,
        fontName='Courier',
        textColor=colors.black,
        leftIndent=10
    )

    # Story (content)
    story = []

    # Parse markdown
    in_table = False
    table_data = []

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()

        # Skip empty lines
        if not line:
            if in_table:
                # End of table
                if table_data:
                    t = Table(table_data)
                    t.setStyle(TableStyle([
                        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('FONTSIZE', (0, 0), (-1, 0), 10),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black),
                        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black)
                    ]))
                    story.append(t)
                    story.append(Spacer(1, 10))
                    table_data = []
                in_table = False
            i += 1
            continue

        # Title (first h1)
        if line.startswith('# ') and len(story) == 0:
            text = line[2:].strip()
            story.append(Paragraph(text, title_style))
            story.append(Spacer(1, 12))

        # H1
        elif line.startswith('# '):
            text = line[2:].strip()
            story.append(PageBreak())
            story.append(Paragraph(text, h1_style))
            story.append(Spacer(1, 12))

        # H2
        elif line.startswith('## '):
            text = line[3:].strip()
            story.append(Paragraph(text, h2_style))
            story.append(Spacer(1, 6))

        # H3
        elif line.startswith('### '):
            text = line[4:].strip()
            story.append(Paragraph(text, h3_style))
            story.append(Spacer(1, 6))

        # H4
        elif line.startswith('#### '):
            text = line[5:].strip()
            story.append(Paragraph(text, h4_style))
            story.append(Spacer(1, 6))

        # Horizontal rule
        elif line.startswith('---'):
            story.append(Spacer(1, 8))

        # Table
        elif '|' in line and not in_table:
            in_table = True
            # Parse table header
            cells = [cell.strip() for cell in line.split('|') if cell.strip()]
            table_data.append(cells)

        elif '|' in line and in_table:
            # Skip separator line
            if re.match(r'\|[\s\-:|]+\|', line):
                i += 1
                continue
            # Parse table row
            cells = [cell.strip() for cell in line.split('|') if cell.strip()]
            table_data.append(cells)

        # Unordered list
        elif line.startswith('- ') or line.startswith('* '):
            text = line[2:].strip()
            # Clean markdown formatting
            text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)  # Bold
            text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)  # Italic
            text = re.sub(r'`(.*?)`', r'<font name="Courier">\1</font>', text)  # Code
            story.append(Paragraph(f'• {text}', normal_style))

        # Numbered list
        elif re.match(r'^\d+\.\s', line):
            text = re.sub(r'^\d+\.\s', '', line).strip()
            # Clean markdown formatting
            text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)  # Bold
            text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)  # Italic
            text = re.sub(r'`(.*?)`', r'<font name="Courier">\1</font>', text)  # Code
            story.append(Paragraph(text, normal_style))

        # Code block
        elif line.startswith('```'):
            # Skip code blocks for simplicity
            i += 1
            while i < len(lines) and not lines[i].startswith('```'):
                i += 1

        # Normal paragraph
        else:
            text = line.strip()
            if text:
                # Clean markdown formatting
                text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)  # Bold
                text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)  # Italic
                text = re.sub(r'`(.*?)`', r'<font name="Courier">\1</font>', text)  # Code
                story.append(Paragraph(text, normal_style))

        i += 1

    # Build PDF
    doc.build(story)
    print(f"[OK] PDF created successfully: {pdf_file}")

if __name__ == "__main__":
    md_file = Path(__file__).parent / "Modelacao_CarrisPlus.md"
    pdf_file = Path(__file__).parent / "Modelacao_CarrisPlus.pdf"

    parse_markdown_to_pdf(md_file, pdf_file)
