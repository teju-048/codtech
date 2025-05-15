import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# Sample Data
data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Sales': [200, 250, 300]
})

# Plot and save chart
plt.bar(data['Month'], data['Sales'], color='skyblue')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
chart_path = "sales_chart.png"
plt.savefig(chart_path)
plt.close()

# Generate PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=16)
pdf.cell(200, 10, txt="Sales Report", ln=True, align='C')
pdf.ln(10)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="This report shows the monthly sales data for Q1. The chart below illustrates the sales trend from January to March.")
pdf.image(chart_path, x=10, y=50, w=180)

pdf.output("sales_report.pdf")
