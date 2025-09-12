from flask import Flask, send_file, render_template_string
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4, portrait
import io, random

app = Flask(__name__)

# -------------------------
# 1ケタの足し算・引き算
# -------------------------
def generate_math_pdf():
    pm_list = ["+", "-"]
    questions, answers = [], []
    num_questions = 20
    generated = set()
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
        que = f"{a} {pm} {b}"
        q = f"({i}) {a} {pm} {b}"
        if que not in generated:
            questions.append(q)
            answers.append(result)
            generated.add(que)
            i += 1

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=portrait(A4))
    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))

    pdf.setFont('HeiseiKakuGo-W5', 25)
    width, height = A4
    pdf.drawCentredString(width/2, height-2*cm, '足し算・引き算（1ケタ）')

    pdf.setFont('Times-Roman', 12)
    start_y = 25.5*cm
    line_h = 0.8*cm
    half = num_questions//2
    for i, q in enumerate(questions):
        if i < half:
            x, y = 2*cm, start_y-(i*line_h*2.5)
        else:
            x, y = 11.5*cm, start_y-((i-half)*line_h*2.5)
        pdf.drawString(x, y, q)

    pdf.setFont('HeiseiKakuGo-W5', 18)
    pdf.drawString(2*cm, 5*cm, '【解答】')
    pdf.setFont('Times-Roman', 12)
    for i, ans in enumerate(answers):
        x = 2*cm+(i%5)*3.5*cm
        y = 4*cm-(i//5)*0.7*cm
        pdf.drawString(x, y, f"({i+1}) {ans}")

    pdf.save()
    buffer.seek(0)
    return buffer


# -------------------------
# 2ケタの足し算・引き算
# -------------------------
def generate_2digit_math_pdf():
    pm_list = ["+", "-"]
    questions, answers = [], []
    num_questions = 20
    generated = set()
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
        que = f"{a} {pm} {b}"
        q = f"({i}) {a} {pm} {b}"
        if que not in generated:
            questions.append(q)
            answers.append(result)
            generated.add(que)
            i += 1

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=portrait(A4))
    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))

    pdf.setFont('HeiseiKakuGo-W5', 25)
    width, height = A4
    pdf.drawCentredString(width/2, height-2*cm, '足し算・引き算（2ケタ）')

    pdf.setFont('Times-Roman', 12)
    start_y = 25.5*cm
    line_h = 0.8*cm
    half = num_questions//2
    for i, q in enumerate(questions):
        if i < half:
            x, y = 2*cm, start_y-(i*line_h*2.5)
        else:
            x, y = 11.5*cm, start_y-((i-half)*line_h*2.5)
        pdf.drawString(x, y, q)

    pdf.setFont('HeiseiKakuGo-W5', 18)
    pdf.drawString(2*cm, 5*cm, '【解答】')
    pdf.setFont('Times-Roman', 12)
    for i, ans in enumerate(answers):
        x = 2*cm+(i%5)*3.5*cm
        y = 4*cm-(i//5)*0.7*cm
        pdf.drawString(x, y, f"({i+1}) {ans}")

    pdf.save()
    buffer.seek(0)
    return buffer


# -------------------------
# 3ケタの足し算・引き算
# -------------------------
def generate_3digit_math_pdf():
    pm_list = ["+", "-"]
    questions, answers = [], []
    num_questions = 20
    generated = set()
    i = 1
    while i <= num_questions:
        pm = random.choice(pm_list)
        if pm == "+":
            a, b = random.randint(1, 999), random.randint(1, 999)
            result = a + b
        else:
            a = random.randint(1, 999)
            b = random.randint(1, a)
            result = a - b
        que = f"{a} {pm} {b}"
        q = f"({i}) {a} {pm} {b}"
        if que not in generated:
            questions.append(q)
            answers.append(result)
            generated.add(que)
            i += 1

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=portrait(A4))
    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))

    pdf.setFont('HeiseiKakuGo-W5', 25)
    width, height = A4
    pdf.drawCentredString(width/2, height-2*cm, '足し算・引き算（3ケタ）')

    pdf.setFont('Times-Roman', 12)
    start_y = 25.5*cm
    line_h = 0.8*cm
    half = num_questions//2
    for i, q in enumerate(questions):
        if i < half:
            x, y = 2*cm, start_y-(i*line_h*2.5)
        else:
            x, y = 11.5*cm, start_y-((i-half)*line_h*2.5)
        pdf.drawString(x, y, q)

    pdf.setFont('HeiseiKakuGo-W5', 18)
    pdf.drawString(2*cm, 5*cm, '【解答】')
    pdf.setFont('Times-Roman', 12)
    for i, ans in enumerate(answers):
        x = 2*cm+(i%5)*3.5*cm
        y = 4*cm-(i//5)*0.7*cm
        pdf.drawString(x, y, f"({i+1}) {ans}")

    pdf.save()
    buffer.seek(0)
    return buffer


# -------------------------
# 1ケタのかけ算
# -------------------------
def generate_1digit_mul_pdf():
    questions, answers = [], []
    num_questions = 20
    generated = set()
    i = 1
    while i <= num_questions:
        a, b = random.randint(0, 9), random.randint(0, 9)
        result = a * b
        que = f" {a} × {b}"
        q = f"({i}) {a} × {b}"   # 修正: "×" を文字列で
        if que not in generated:
            questions.append(q)
            answers.append(result)
            generated.add(que)
            i += 1

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=portrait(A4))
    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))

    pdf.setFont('HeiseiKakuGo-W5', 25)
    width, height = A4
    pdf.drawCentredString(width/2, height-2*cm, 'かけ算（1ケタ）')

    pdf.setFont('Times-Roman', 12)
    start_y = 25.5*cm
    line_h = 0.8*cm
    half = num_questions//2
    for i, q in enumerate(questions):
        if i < half:
            x, y = 2*cm, start_y-(i*line_h*2.5)
        else:
            x, y = 11.5*cm, start_y-((i-half)*line_h*2.5)
        pdf.drawString(x, y, q)

    pdf.setFont('HeiseiKakuGo-W5', 18)
    pdf.drawString(2*cm, 5*cm, '【解答】')
    pdf.setFont('Times-Roman', 12)
    for i, ans in enumerate(answers):
        x = 2*cm+(i%5)*3.5*cm
        y = 4*cm-(i//5)*0.7*cm
        pdf.drawString(x, y, f"({i+1}) {ans}")

    pdf.save()
    buffer.seek(0)
    return buffer

# -------------------------
# 2ケタのかけ算
# -------------------------
def generate_2digit_mul_pdf():
    questions, answers = [], []
    num_questions = 20
    generated = set()
    i = 1
    while i <= num_questions:
        a, b = random.randint(0, 99), random.randint(0, 99)
        result = a * b
        que = f" {a} × {b}"
        q = f"({i}) {a} × {b}"   # 修正: "×" を文字列で
        if que not in generated:
            questions.append(q)
            answers.append(result)
            generated.add(que)
            i += 1

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=portrait(A4))
    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))

    pdf.setFont('HeiseiKakuGo-W5', 25)
    width, height = A4
    pdf.drawCentredString(width/2, height-2*cm, 'かけ算（2ケタ）')

    pdf.setFont('Times-Roman', 12)
    start_y = 25.5*cm
    line_h = 0.8*cm
    half = num_questions//2
    for i, q in enumerate(questions):
        if i < half:
            x, y = 2*cm, start_y-(i*line_h*2.5)
        else:
            x, y = 11.5*cm, start_y-((i-half)*line_h*2.5)
        pdf.drawString(x, y, q)

    pdf.setFont('HeiseiKakuGo-W5', 18)
    pdf.drawString(2*cm, 5*cm, '【解答】')
    pdf.setFont('Times-Roman', 12)
    for i, ans in enumerate(answers):
        x = 2*cm+(i%5)*3.5*cm
        y = 4*cm-(i//5)*0.7*cm
        pdf.drawString(x, y, f"({i+1}) {ans}")

    pdf.save()
    buffer.seek(0)
    return buffer# -------------------------
# 3ケタのかけ算
# -------------------------
def generate_3digit_mul_pdf():
    questions, answers = [], []
    num_questions = 20
    generated = set()
    i = 1
    while i <= num_questions:
        a, b = random.randint(0, 999), random.randint(0, 999)
        result = a * b
        que = f" {a} × {b}"
        q = f"({i}) {a} × {b}"   # 修正: "×" を文字列で
        if que not in generated:
            questions.append(q)
            answers.append(result)
            generated.add(que)
            i += 1

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=portrait(A4))
    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))

    pdf.setFont('HeiseiKakuGo-W5', 25)
    width, height = A4
    pdf.drawCentredString(width/2, height-2*cm, 'かけ算（3ケタ）')

    pdf.setFont('Times-Roman', 12)
    start_y = 25.5*cm
    line_h = 0.8*cm
    half = num_questions//2
    for i, q in enumerate(questions):
        if i < half:
            x, y = 2*cm, start_y-(i*line_h*2.5)
        else:
            x, y = 11.5*cm, start_y-((i-half)*line_h*2.5)
        pdf.drawString(x, y, q)

    pdf.setFont('HeiseiKakuGo-W5', 18)
    pdf.drawString(2*cm, 5*cm, '【解答】')
    pdf.setFont('Times-Roman', 12)
    for i, ans in enumerate(answers):
        x = 2*cm+(i%5)*3.5*cm
        y = 4*cm-(i//5)*0.7*cm
        pdf.drawString(x, y, f"({i+1}) {ans}")

    pdf.save()
    buffer.seek(0)
    return buffer

# -------------------------
# 1ケタのわり算
# -------------------------
def generate_1digit_div_pdf():
    questions, answers = [], []
    num_questions = 20
    generated = set()
    i = 1
    while i <= num_questions:
        b = random.randint(1, 9)          # 割る数
        result = random.randint(1, 9)     # 答えを先に決める
        a = b * result                    # 割られる数（必ず割り切れる）

        q_text = f"({i}) {a} ÷ {b}"
        if q_text not in generated:
            questions.append(q_text)
            answers.append(result)
            generated.add(q_text)
            i += 1

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=portrait(A4))
    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))

    # タイトル
    pdf.setFont('HeiseiKakuGo-W5', 25)
    width, height = A4
    pdf.drawCentredString(width / 2, height - 2 * cm, 'わり算（1ケタ）')

    # 問題
    pdf.setFont('Times-Roman', 12)
    start_y = 25.5 * cm
    line_h = 0.8 * cm
    half = num_questions // 2
    for i, q in enumerate(questions):
        if i < half:
            x, y = 2 * cm, start_y - (i * line_h * 2.5)
        else:
            x, y = 11.5 * cm, start_y - ((i - half) * line_h * 2.5)
        pdf.drawString(x, y, q)

    # 解答
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
# 2ケタのわり算
# -------------------------
def generate_2digit_div_pdf():
    questions, answers = [], []
    num_questions = 20
    generated = set()
    i = 1
    while i <= num_questions:
        b = random.randint(1, 99)          # 割る数
        result = random.randint(1, 9)     # 答えを先に決める
        a = b * result                    # 割られる数（必ず割り切れる）

        q_text = f"({i}) {a} ÷ {b}"
        if q_text not in generated:
            questions.append(q_text)
            answers.append(result)
            generated.add(q_text)
            i += 1

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=portrait(A4))
    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))

    # タイトル
    pdf.setFont('HeiseiKakuGo-W5', 25)
    width, height = A4
    pdf.drawCentredString(width / 2, height - 2 * cm, 'わり算（2ケタ）')

    # 問題
    pdf.setFont('Times-Roman', 12)
    start_y = 25.5 * cm
    line_h = 0.8 * cm
    half = num_questions // 2
    for i, q in enumerate(questions):
        if i < half:
            x, y = 2 * cm, start_y - (i * line_h * 2.5)
        else:
            x, y = 11.5 * cm, start_y - ((i - half) * line_h * 2.5)
        pdf.drawString(x, y, q)

    # 解答
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
# 3ケタのわり算
# -------------------------
def generate_3digit_div_pdf():
    questions, answers = [], []
    num_questions = 20
    generated = set()
    i = 1
    while i <= num_questions:
        b = random.randint(1, 999)          # 割る数
        result = random.randint(1, 99)     # 答えを先に決める
        a = b * result                    # 割られる数（必ず割り切れる）

        q_text = f"({i}) {a} ÷ {b}"
        if q_text not in generated:
            questions.append(q_text)
            answers.append(result)
            generated.add(q_text)
            i += 1

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=portrait(A4))
    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))

    # タイトル
    pdf.setFont('HeiseiKakuGo-W5', 25)
    width, height = A4
    pdf.drawCentredString(width / 2, height - 2 * cm, 'わり算（3ケタ）')

    # 問題
    pdf.setFont('Times-Roman', 12)
    start_y = 25.5 * cm
    line_h = 0.8 * cm
    half = num_questions // 2
    for i, q in enumerate(questions):
        if i < half:
            x, y = 2 * cm, start_y - (i * line_h * 2.5)
        else:
            x, y = 11.5 * cm, start_y - ((i - half) * line_h * 2.5)
        pdf.drawString(x, y, q)

    # 解答
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
# Flask ルーティング
# -------------------------
@app.route("/")
def index():
    return render_template_string('''
    <h1>計算問題PDF生成</h1>
    <ul>
        <li><a href="/pm_1digit" target="_blank">1ケタの足し算・引き算</a></li>
        <li><a href="/pm_2digit" target="_blank">2ケタの足し算・引き算</a></li>
        <li><a href="/pm_3digit" target="_blank">3ケタの足し算・引き算</a></li>
        <li><a href="/mul_1digit" target="_blank">1ケタのかけ算</a></li>
        <li><a href="/mul_2digit" target="_blank">2ケタのかけ算</a></li>
        <li><a href="/mul_3digit" target="_blank">3ケタのかけ算</a></li>
        <li><a href="/div_1digit" target="_blank">1ケタのわり算</a></li>
        <li><a href="/div_2digit" target="_blank">2ケタのわり算</a></li>
        <li><a href="/div_3digit" target="_blank">3ケタのわり算</a></li>
    </ul>
    ''')

@app.route("/pm_1digit")
def generate_pdf_1digit():
    pdf_buffer = generate_math_pdf()
    return send_file(pdf_buffer, mimetype="application/pdf",
                     download_name="足し算・引き算（1ケタ）.pdf")

@app.route("/pm_2digit")
def generate_pdf_2digit():
    pdf_buffer = generate_2digit_math_pdf()
    return send_file(pdf_buffer, mimetype="application/pdf",
                     download_name="足し算・引き算（2ケタ）.pdf")

@app.route("/pm_3digit")
def generate_pdf_3digit():
    pdf_buffer = generate_3digit_math_pdf()
    return send_file(pdf_buffer, mimetype="application/pdf",
                     download_name="足し算・引き算（3ケタ）.pdf")

@app.route("/mul_1digit")
def generate_pdf_1digit_mul():
    pdf_buffer = generate_1digit_mul_pdf()
    return send_file(pdf_buffer, mimetype="application/pdf",
                     download_name="かけ算（1ケタ）.pdf")

@app.route("/mul_2digit")
def generate_pdf_2digit_mul():
    pdf_buffer = generate_2digit_mul_pdf()
    return send_file(pdf_buffer, mimetype="application/pdf",
                     download_name="かけ算（2ケタ）.pdf")

@app.route("/mul_3digit")
def generate_pdf_3digit_mul():
    pdf_buffer = generate_3digit_mul_pdf()
    return send_file(pdf_buffer, mimetype="application/pdf",
                     download_name="かけ算（3ケタ）.pdf")

@app.route("/div_1digit")
def generate_pdf_1digit_div():
    pdf_buffer = generate_1digit_div_pdf()
    return send_file(pdf_buffer, mimetype="application/pdf",
                     download_name="わり算（1ケタ）.pdf")

@app.route("/div_2digit")
def generate_pdf_2digit_div():
    pdf_buffer = generate_2digit_div_pdf()
    return send_file(pdf_buffer, mimetype="application/pdf",
                     download_name="わり算（2ケタ）.pdf")

@app.route("/div_3digit")
def generate_pdf_3digit_div():
    pdf_buffer = generate_3digit_div_pdf()
    return send_file(pdf_buffer, mimetype="application/pdf",
                     download_name="わり算（3ケタ）.pdf")


if __name__ == "__main__":
    app.run(debug=True)
