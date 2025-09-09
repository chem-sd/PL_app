from flask import Flask, Response, send_file, render_template_string
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4, portrait
import io, random, datetime

app = Flask(__name__)

# -------------------------
# 1桁の計算問題 PDF
# -------------------------
def generate_math_pdf():
    pm_list = ["+", "-"]
    questions, answers = [], []
    num_questions = 20
    generated_problems_set = set()
    i = 1
    while i <= num_questions:
        pm = random.choice(pm_list)
        if pm == "+":
            a, b = random.randint(0, 9), random.randint(0, 9)
            result = a + b
        else:
            a = random.randint(0, 9)
            b = random.randint(0, a)
            result = a - b
        q_text = f"({i}) {a} {pm} {b}"
        if q_text not in generated_problems_set:
            questions.append(q_text)
            answers.append(result)
            generated_problems_set.add(q_text)
            i += 1

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=portrait(A4))
    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))

    pdf.setFont('HeiseiKakuGo-W5', 25)
    width, height = A4
    pdf.drawCentredString(width / 2, height - 2 * cm, '計算問題（1ケタ）')

    pdf.setFont('Times-Roman', 12)
    start_y = 25.5 * cm
    line_height = 0.8 * cm
    half = num_questions // 2
    for i, q in enumerate(questions):
        if i < half:
            x, y = 2 * cm, start_y - (i * line_height * 2.5)
        else:
            x, y = 11.5 * cm, start_y - ((i - half) * line_height * 2.5)
        pdf.drawString(x, y, q)

    pdf.setFont('HeiseiKakuGo-W5', 18)
    pdf.drawString(2 * cm, 5 * cm, '【解答】')
    pdf.setFont('Times-Roman', 12)
    for i, ans in enumerate(answers):
        x = 2 * cm + (i % 5) * 3.5 * cm
        y = 4 * cm - (i // 5) * 0.7 * cm
        pdf.drawString(x, y, f"({i+1}) {ans}")

    pdf.save()
    buffer.seek(0)
    return buffer


# -------------------------
# 2桁の計算問題 PDF
# -------------------------
def generate_2digit_math_pdf():
    pm_list = ["+", "-"]
    questions, answers = [], []
    num_questions = 20
    generated_problems_set = set()
    i = 1
    while i <= num_questions:
        pm = random.choice(pm_list)
        if pm == "+":
            a, b = random.randint(1, 99), random.randint(1, 99)
            result = a + b
        else:
            a = random.randint(1, 99)
            b = random.randint(1, a)
            result = a - b
        q_text = f"({i}) {a} {pm} {b}"
        if q_text not in generated_problems_set:
            questions.append(q_text)
            answers.append(result)
            generated_problems_set.add(q_text)
            i += 1

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=portrait(A4))
    pdf.saveState()
    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))

    title_text = "足し算・引き算（2ケタ）"
    pdf.setFont('HeiseiKakuGo-W5', 25)
    width, height = A4
    pdf.drawCentredString(width / 2, height - 2 * cm, title_text)

    # 問題
    pdf.setFont('Times-Roman', 12)
    start_y = 25.5 * cm
    line_height = 0.8 * cm
    half = num_questions // 2
    for i, q in enumerate(questions):
        if i < half:
            x, y = 2 * cm, start_y - (i * line_height * 2.5)
        else:
            x, y = 11.5 * cm, start_y - ((i - half) * line_height * 2.5)
        pdf.drawString(x, y, q)

    # 解答
    pdf.setFont('HeiseiKakuGo-W5', 18)
    pdf.drawString(2 * cm, 5 * cm, '【解答】')
    pdf.setFont('Times-Roman', 12)
    for i, ans in enumerate(answers):
        x = 2 * cm + (i % 5) * 3.5 * cm
        y = 4 * cm - (i // 5) * 0.7 * cm
        pdf.drawString(x, y, f"({i+1}) {ans}")

    pdf.restoreState()
    pdf.save()
    buffer.seek(0)
    return buffer


# -------------------------
# Flask ルーティング
# -------------------------
@app.route("/")
def index():
    return render_template_string('''
    <h1>計算問題PDF生成</h1>
    <ul>
        <li><a href="/pm_1digit" target="_blank">1ケタの計算問題</a></li>
        <li><a href="/pm_2digit" target="_blank">2ケタの計算問題</a></li>
    </ul>
    ''')

@app.route("/pm_1digit")
def generate_pdf_1digit():
    pdf_buffer = generate_math_pdf()
    file_name_1 = "足し算・引き算（1ケタ）.pdf"
    return send_file(
        pdf_buffer,
        mimetype="application/pdf",
        download_name=file_name_1
    )

@app.route("/pm_2digit")
def generate_pdf_2digit():
    pdf_buffer = generate_2digit_math_pdf()
    file_name_2 = "足し算・引き算（2ケタ）.pdf"
    return send_file(
        pdf_buffer,
        mimetype="application/pdf",
        download_name=file_name_2
    )



if __name__ == "__main__":
    app.run(debug=True)

