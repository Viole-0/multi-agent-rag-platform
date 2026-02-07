from fpdf import FPDF
import os
import textwrap

FONT_PATH = os.path.join("assets", "DejaVuSans.ttf")

def safe_multicell(pdf, text, line_height=8, width=180):
    """
    Safely write long text to PDF by wrapping it
    and resetting margins to avoid fpdf2 overflow errors.
    """
    pdf.set_x(10)  # reset left margin
    wrapped = textwrap.fill(text, width=90)
    pdf.multi_cell(width, line_height, wrapped)

def export_pdf(insights, filename="tech_intelligence_report.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.add_font("DejaVu", "", FONT_PATH, uni=True)
    pdf.set_font("DejaVu", size=12)

    # Title
    pdf.set_x(10)
    pdf.cell(0, 10, "Technology Intelligence Report", ln=True)
    pdf.ln(5)

    # TRL
    safe_multicell(pdf, f"TRL: {insights['trl']}")
    pdf.ln(2)

    # Velocity
    safe_multicell(pdf, f"Trend Velocity: {insights['velocity']}")
    pdf.ln(2)

    # Forecast
    pdf.set_x(10)
    pdf.cell(0, 8, "Forecast:", ln=True)
    safe_multicell(pdf, insights["forecast"])
    pdf.ln(2)

    # Narrative
    pdf.set_x(10)
    pdf.cell(0, 8, "Strategic Narrative:", ln=True)
    safe_multicell(pdf, insights["narrative"])

    pdf.output(filename)
    return os.path.abspath(filename)
