from fpdf import FPDF

'''

get the shirtficate.png on https://cs50.harvard.edu/python/psets/6/shirt/shirt.png

'''


user = input("Name: ")

pdf = FPDF()

pdf.add_page(orientation="P", format="A4")
pdf.set_font("helvetica", "b", 40)
pdf.cell(0, 40, "CS50 SHIRTIFICATE", align="C")
pdf.image("shirtificate.png", 10, 60, 190)
pdf.set_text_color(255, 255, 255)
largura = pdf.w - pdf.l_margin - pdf.r_margin
x = pdf.l_margin + (largura - pdf.get_string_width(f"{user} Took CS50")) / 2
pdf.set_xy(x, 130)
pdf.write(25, f"{user} Took CS50")
pdf.output("shirtificate.pdf")