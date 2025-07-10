import webbrowser
from fpdf import FPDF

class Bill:
    """
    Object that contains a data about a bill, such as total
    amount and period of the bill...
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period
     
class Flatmate:
    """
    Create a flatmate person who lives in the flat and
    pays a share of the bill...
    """

    def __init__(self, name, days_in_home):
        self.name = name
        self.days_in_home = days_in_home

    def pays(self, bi_ll, other_flatmate):
        weight = self.days_in_home / (self.days_in_home + other_flatmate.days_in_home)
        return bill.amount * weight
class PdfReport:
    """
    Creates a Pdf file that contains data about the flatmates such
    as their names, their due amounts and the period of the bill...
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation = "P", unit = "pt", format="A4")
        pdf.add_page()
        pdf.image("house.png", w=30,h=30)
        pdf.set_font(family="Times", size=24, style="IBU")
        pdf.set_text_color(0,255,0)
        pdf.cell(w = 0, h = 80, txt="Flatmates Bill", border=1, align="C", ln=1)
        pdf.set_font(family="Times", size=18, style="B")
        pdf.set_text_color(255, 0, 0)
        pdf.cell(w=300, h=40, txt="Month & Year:", border=1)
        pdf.cell(w=240, h=40, txt=bill.period, border=1, ln=1)
        pdf.set_font(family="Times", size=16, style="")
        pdf.set_text_color(0, 0, 255)
        pdf.cell(w=300, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=240, h=40, txt=str(round(flatmate1.pays(bill, flatmate2), 2)), border=1, ln=1)
        pdf.set_font(family="Times", size=16, style="")
        pdf.set_text_color(0, 255, 0)
        pdf.cell(w=300, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=240, h=40, txt=str(round(flatmate2.pays(bill, flatmate1), 2)), border=1)
        pdf.output(self.filename)
        webbrowser.open(self.filename)

amount = float(input("Enter the bill amount: "))
m_d = str(input("Enter the current Month & Year (E.g. December 2020) :"))
f1_name = str(input("Enter the name of the flatmate 1:"))
f1_days = int(input(f"Enter the number of days in home ({f1_name}): "))
f2_name = str(input("Enter the name of the flatmate 2:"))
f2_days = int(input(f"Enter the number of days in home ({f2_name}): "))
bill = Bill(amount,m_d)
flatmate1 = Flatmate(f1_name, f1_days)
flatmate2 = Flatmate(f2_name, f2_days)

print(f1_name, " pays:", flatmate1.pays(bill, flatmate2))
print(f2_name, " pays:", flatmate2.pays(bill, flatmate1))

pdf_report = PdfReport("Bill.pdf")
pdf_report.generate(flatmate1,flatmate2,bill)