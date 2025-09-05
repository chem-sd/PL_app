from flask import Flask, Response
from reportlab.pdfgen import canvas
import io, random

app = Flask(__name__)

@app.route("/generate_pdf")
def generate_pdf():
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.drawString(100, 750, f"ランダム数: {random.randint(1,100)}")
    pdf.save()
    buffer.seek(0)

    return Response(buffer, mimetype="application/pdf")

@app.route("/")
def index():
    return '<a href="/generate_pdf" target="_blank">PDFを生成</a>'

if __name__ == "__main__":
    app.run()
