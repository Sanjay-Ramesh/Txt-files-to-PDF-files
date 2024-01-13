import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("Text+Files\\*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    df = filepath
    
    pdf.add_page()
    filename = Path(filepath).stem
    title = filename.title()
    pdf.set_font(family="Times", size=18, style="B")
    pdf.cell(w=0, h=10, txt=title, ln=1)

    with open(filepath, 'r') as file:
        content = file.read()

    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output(f"PDFS\\output.pdf")
