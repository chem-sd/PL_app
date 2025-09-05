#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io, sys, random, datetime
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4, portrait

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

    # タイトル
    pdf.setFont('HeiseiKakuGo-W5', 25)
    width, height = A4
    pdf.drawCentredString(width / 2, height - 2 * cm, '計算問題')

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

    pdf.save()
    buffer.seek(0)
    return buffer

# --- CGIとしてPDFを返す ---
pdf_buffer = generate_math_pdf()
sys.stdout.write("Content-Type: application/pdf\n\n")
sys.stdout.flush()
sys.stdout.buffer.write(pdf_buffer.getvalue())
