from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_report(content, filename="ERIA_Report.pdf"):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "Education Regulation Impact Analyzer (ERIA)",
            styles['Title']
        )
    )

    story.append(Spacer(1, 12))

    story.append(
        Paragraph(
            content.replace("\n", "<br/>"),
            styles['BodyText']
        )
    )

    doc.build(story)

    return filename