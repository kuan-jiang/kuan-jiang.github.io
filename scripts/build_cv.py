from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer


OUTPUT = "files/CV.pdf"
BLUE = colors.HexColor("#0056A6")
TEXT = colors.HexColor("#202124")
MUTED = colors.HexColor("#5F6368")
RULE = colors.HexColor("#D9DEE5")


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.5)
    canvas.line(0.65 * inch, 0.48 * inch, 7.85 * inch, 0.48 * inch)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(0.65 * inch, 0.3 * inch, "Kuan Jiang - Academic CV")
    canvas.drawRightString(7.85 * inch, 0.3 * inch, f"Page {doc.page}")
    canvas.restoreState()


doc = BaseDocTemplate(
    OUTPUT,
    pagesize=letter,
    rightMargin=0.65 * inch,
    leftMargin=0.65 * inch,
    topMargin=0.55 * inch,
    bottomMargin=0.62 * inch,
    title="Academic CV - Kuan Jiang",
    author="Kuan Jiang",
)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
doc.addPageTemplates(PageTemplate(id="cv", frames=[frame], onPage=footer))

styles = getSampleStyleSheet()
name = ParagraphStyle(
    "Name", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=23,
    leading=26, textColor=TEXT, alignment=TA_LEFT, spaceAfter=2,
)
role = ParagraphStyle(
    "Role", parent=styles["Normal"], fontName="Helvetica", fontSize=10.5,
    leading=14, textColor=MUTED, spaceAfter=4,
)
contact = ParagraphStyle(
    "Contact", parent=styles["Normal"], fontName="Helvetica", fontSize=9,
    leading=12, textColor=BLUE, spaceAfter=10,
)
section = ParagraphStyle(
    "Section", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=10.5,
    leading=13, textColor=BLUE, spaceBefore=7, spaceAfter=4,
    borderColor=RULE, borderWidth=0, borderPadding=0,
)
item = ParagraphStyle(
    "Item", parent=styles["Normal"], fontName="Helvetica", fontSize=9,
    leading=12.2, textColor=TEXT, leftIndent=9, firstLineIndent=-6, spaceAfter=3,
)
publication = ParagraphStyle(
    "Publication", parent=item, leading=12.5, spaceAfter=5,
)

story = [
    Paragraph("Kuan Jiang", name),
    Paragraph("PhD Candidate in Statistics, North Carolina State University", role),
    Paragraph(
        '<link href="mailto:kjiang6@ncsu.edu" color="#0056A6">kjiang6@ncsu.edu</link>'
        ' &nbsp;|&nbsp; <link href="https://kuan-jiang.github.io/" color="#0056A6">kuan-jiang.github.io</link>'
        ' &nbsp;|&nbsp; <link href="https://orcid.org/0009-0001-2935-5425" color="#0056A6">ORCID 0009-0001-2935-5425</link>',
        contact,
    ),
    Paragraph("EDUCATION", section),
    Paragraph("- <b>PhD Candidate in Statistics</b>, North Carolina State University, 2025-Present", item),
    Paragraph("- <b>Master's degree in Epidemiology and Biostatistics</b>, Peking University, September 2022-July 2025", item),
    Paragraph("- <b>Bachelor of Medicine in Preventive Medicine</b>, Peking University, 2018-2023", item),
    Paragraph("- <b>Bachelor of Economics (Dual Degree)</b>, Peking University, 2018-2023", item),
    Paragraph("RESEARCH INTERESTS", section),
    Paragraph("- Causal inference; data fusion; health and clinical data analysis", item),
    Paragraph("PUBLICATIONS", section),
    Paragraph(
        '- <b>Kuan Jiang</b>, Wenjie Hu, Xinxing Lai, Shu Yang, and Xiao-Hua Zhou. '
        '"Improving Sensitivity Analysis by Synthesizing Randomized Clinical Trials With Limited Overlap." '
        '<i>Statistics in Medicine</i> 45(18-19), e70637 (2026). '
        '<link href="https://doi.org/10.1002/sim.70637" color="#0056A6">doi:10.1002/sim.70637</link>',
        publication,
    ),
    Paragraph(
        '- <b>Kuan Jiang</b>, Xin-Xing Lai, Shu Yang, Ying Gao, and Xiao-Hua Zhou. '
        '"A Practical Analysis Procedure on Generalizing Comparative Effectiveness in the Randomized Clinical Trial '
        'to the Real-World Trial-Eligible Population." <i>Journal of Biopharmaceutical Statistics</i> '
        '35(6), 1196-1208 (2025). '
        '<link href="https://doi.org/10.1080/10543406.2025.2489282" color="#0056A6">doi:10.1080/10543406.2025.2489282</link>',
        publication,
    ),
    Paragraph("SELECTED RESEARCH EXPERIENCE", section),
    Paragraph("- Research Assistant, Institute for Brain Disorders, Beijing University of Chinese Medicine", item),
    Paragraph("TEACHING EXPERIENCE", section),
    Paragraph("- Teaching Assistant, ST 308, North Carolina State University", item),
    Paragraph("- Teaching Assistant, ST 371E, North Carolina State University", item),
    Paragraph("SKILLS", section),
    Paragraph("- R, Python, Stata, LaTeX", item),
]

doc.build(story)
