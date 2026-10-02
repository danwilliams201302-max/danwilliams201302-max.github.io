from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

OUTPUT = "/workspace/scratch/3cd3df426f2f/dw-modern-site/dist/assets/dw-transport-readiness-checklist.pdf"

pdfmetrics.registerFont(TTFont("DWRegular", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DWBold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))

navy = colors.HexColor("#07111f")
ink = colors.HexColor("#172033")
muted = colors.HexColor("#506074")
teal = colors.HexColor("#14c9ae")
line = colors.HexColor("#dce4ee")
paper = colors.HexColor("#f7fafc")

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    rightMargin=15*mm,
    leftMargin=15*mm,
    topMargin=13*mm,
    bottomMargin=12*mm,
    title="DW Transport Consultancy - Transport Admin and Compliance Readiness Checklist",
    author="DW Transport Consultancy",
)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleDW", parent=styles["Title"], fontName="DWBold", fontSize=22, leading=24, textColor=colors.white, spaceAfter=2))
styles.add(ParagraphStyle(name="SubDW", parent=styles["Normal"], fontName="DWRegular", fontSize=9.5, leading=12, textColor=colors.HexColor("#c9d6e6")))
styles.add(ParagraphStyle(name="SectionDW", parent=styles["Heading2"], fontName="DWBold", fontSize=11.5, leading=14, textColor=ink, spaceBefore=5, spaceAfter=4))
styles.add(ParagraphStyle(name="ItemDW", parent=styles["Normal"], fontName="DWRegular", fontSize=8.5, leading=10.5, textColor=ink))
styles.add(ParagraphStyle(name="SmallDW", parent=styles["Normal"], fontName="DWRegular", fontSize=7.5, leading=9.5, textColor=muted))
styles.add(ParagraphStyle(name="FooterDW", parent=styles["Normal"], fontName="DWRegular", fontSize=7.2, leading=9, textColor=colors.HexColor("#d5e1ef")))

def checkbox_item(text):
    return [Paragraph("<b>□</b>", styles["ItemDW"]), Paragraph(text, styles["ItemDW"]), Paragraph("R / A / G", styles["SmallDW"])]

story = []
header = Table([
    [Paragraph("DW Transport Consultancy", styles["TitleDW"])],
    [Paragraph("Transport Admin & Compliance Readiness Checklist", styles["SubDW"])],
], colWidths=[180*mm])
header.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), navy),
    ("LEFTPADDING", (0,0), (-1,-1), 8),
    ("RIGHTPADDING", (0,0), (-1,-1), 8),
    ("TOPPADDING", (0,0), (-1,0), 10),
    ("BOTTOMPADDING", (0,0), (-1,0), 0),
    ("TOPPADDING", (0,1), (-1,1), 0),
    ("BOTTOMPADDING", (0,1), (-1,1), 10),
]))
story.append(header)
story.append(Spacer(1, 5*mm))
story.append(Paragraph("Use this as a quick sense-check. Tick the evidence you can find quickly, mark anything unclear, and focus first on the red items. It is an operational checklist, not a formal legal or compliance sign-off.", styles["SmallDW"]))
story.append(Spacer(1, 2*mm))

sections = [
    ("1. Operator licence and core records", [
        "Current operator licence details and operating centre information are easy to find.",
        "Maintenance arrangements, inspection intervals and defect reporting are documented.",
        "The person responsible for each key record and action is clear.",
        "Important correspondence, decisions and evidence can be retrieved without a panic search.",
    ]),
    ("2. Drivers and workforce", [
        "Driver entitlement, training and required checks are current and recorded.",
        "Tacho, working time, infringements and follow-up actions are reviewed consistently.",
        "Absence, agency cover, handovers and fatigue concerns are visible to the right person.",
        "Drivers know how to report defects, incidents, delays and changes to the plan.",
    ]),
    ("3. Vehicles, defects and evidence", [
        "Vehicle inspections, defects, repairs and safety-critical follow-ups are easy to trace.",
        "Dashcam, telematics, tacho and maintenance evidence can be linked to the right vehicle or job.",
        "There is a clear process for taking a vehicle out of service and returning it to work.",
        "Repeated defects, incidents or breakdown patterns are reviewed rather than simply closed.",
    ]),
    ("4. Planning, handovers and customer updates", [
        "One reliable version of the plan exists for the traffic office, drivers and management.",
        "Collection, delivery, ETA, delay and exception information is updated once and shared clearly.",
        "The same job details are not being re-keyed across several spreadsheets or systems.",
        "The operation can explain what happened when a customer queries a delay or invoice.",
    ]),
    ("5. Reporting and improvement", [
        "Management reports match what actually happened in the operation.",
        "The team can see avoidable admin, missed handovers, waiting time and repeated chasing.",
        "Actions have an owner, a due date and a way to show whether the change worked.",
        "Automation or AI is being considered only where the underlying process and data are clear.",
    ]),
]

for title, items in sections:
    story.append(Paragraph(title, styles["SectionDW"]))
    rows = [checkbox_item(item) for item in items]
    table = Table(rows, colWidths=[8*mm, 157*mm, 15*mm], rowHeights=[7.2*mm]*len(rows))
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), paper),
        ("BOX", (0,0), (-1,-1), .5, line),
        ("INNERHORIZONTAL", (0,0), (-1,-1), .35, line),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 5),
        ("RIGHTPADDING", (0,0), (-1,-1), 5),
        ("TOPPADDING", (0,0), (-1,-1), 2),
        ("BOTTOMPADDING", (0,0), (-1,-1), 2),
        ("TEXTCOLOR", (0,0), (0,-1), teal),
        ("ALIGN", (0,0), (0,-1), "CENTER"),
        ("ALIGN", (2,0), (2,-1), "RIGHT"),
    ]))
    story.append(table)

story.append(Spacer(1, 3*mm))
actions = Table([
    [Paragraph("Three actions worth reviewing first", styles["SectionDW"]), ""],
    [Paragraph("1.", styles["ItemDW"]), Paragraph("Where is the same information being entered, checked or chased more than once?", styles["ItemDW"])],
    [Paragraph("2.", styles["ItemDW"]), Paragraph("What evidence would take too long to find if there were an incident, dispute or audit question tomorrow?", styles["ItemDW"])],
    [Paragraph("3.", styles["ItemDW"]), Paragraph("Which small repeated task could be removed, automated or made visible first?", styles["ItemDW"])],
], colWidths=[10*mm, 170*mm])
actions.setStyle(TableStyle([
    ("SPAN", (0,0), (-1,0)),
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#e5fbf6")),
    ("BOX", (0,0), (-1,-1), .6, teal),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 7),
    ("RIGHTPADDING", (0,0), (-1,-1), 7),
    ("TOPPADDING", (0,0), (-1,-1), 4),
    ("BOTTOMPADDING", (0,0), (-1,-1), 4),
]))
story.append(actions)
story.append(Spacer(1, 4*mm))
footer = Table([[Paragraph("Want to talk through the result? Email dwtransportconsultancy@gmail.com for a 20-minute review. UK based, with full EU coverage.", styles["FooterDW"])]], colWidths=[180*mm])
footer.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), navy),
    ("LEFTPADDING", (0,0), (-1,-1), 8),
    ("RIGHTPADDING", (0,0), (-1,-1), 8),
    ("TOPPADDING", (0,0), (-1,-1), 7),
    ("BOTTOMPADDING", (0,0), (-1,-1), 7),
]))
story.append(footer)

doc.build(story)
