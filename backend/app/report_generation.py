from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer

from reportlab.lib.styles import getSampleStyleSheet


def generate_report( filename,patient_data,prediction_results):
    doc =SimpleDocTemplate(filename)
    styles= getSampleStyleSheet()
    elements=[]
    title=Paragraph("AI Health Prediction Report",styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 20))
    for key, value in patient_data.items():
        patient_text=Paragraph(f"<b>{key}</b>: {value}",styles["BodyText"])
        elements.append(patient_text)
    elements.append(Spacer(1, 20))
    for result in prediction_results:
        disease=Paragraph(f"<b>Disease:</b> "f"{result['disease']}",styles["BodyText"])
        probability =Paragraph(f"<b>Risk:</b> "f"{result['probability']}%", styles["BodyText"])
        reason= Paragraph(f"<b>Reason:</b> "f"{result['reason']}",styles["BodyText"])
        remedy= Paragraph(f"<b>Remedy:</b> "f"{result['remedy']}",styles["BodyText"])
        elements.append(disease)
        elements.append(probability)
        elements.append(reason)
        elements.append(remedy)
        elements.append(Spacer(1, 15))
    doc.build(elements)
