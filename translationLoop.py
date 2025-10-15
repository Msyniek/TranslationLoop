import os
import pdfplumber
import translators as ts
from PyPDF2 import PdfReader
from reportlab.pdfgen import canvas
from tkinter.filedialog import askopenfilename
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

# Function to read the text from a PDF file
def extract_text_from_pdf(pdf_path):
    text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text

# Function to write the translated text into a new PDF file
def save_text_to_pdf(text_chunks, output_pdf_path):
    styles = getSampleStyleSheet()
    story = []
    for chunk in text_chunks:
        # For better separation, split into lines and wrap each line as a Paragraph
        for line in chunk.splitlines():
            if line.strip():
                story.append(Paragraph(line, styles['Normal']))
                story.append(Spacer(1, 12))  # add space between lines
    doc = SimpleDocTemplate(output_pdf_path, pagesize=letter)
    doc.build(story)

# Path to the input PDF
input_pdf_path = os.path.join(os.path.dirname(__file__), askopenfilename(title="Select PDF file to translate"))
output_pdf_path = os.path.join(os.path.dirname(__file__), input("Enter output PDF file name (with .pdf extension): "))

user_translator = input("Choose translator (default: yandex) or https://github.com/UlionTse/translators/tree/master?tab=readme-ov-file ").strip() or 'yandex'
user_delay = input("Enter delay between requests in seconds (default: 3): ").strip() or 3
user_language = input("Enter target language code (default: en): ").strip() or 'en'
user_split = int(input("Enter character limit per chunk (default: 3800): ").strip() or 3800)

# Extract text from the input PDF
text = extract_text_from_pdf(input_pdf_path)

# Function to split text into chunks based on the character limit
def chunk_text(text, limit = user_split):
    chunks = []
    while len(text) > limit:
        chunk = text[:limit]
        chunks.append(chunk)
        text = text[limit:]
    chunks.append(text)
    return chunks

# Split the extracted text into chunks
chunks = chunk_text(text)

# Translate each chunk and store the results
translated_chunks = [ts.translate_text(chunk, to_language=user_language, translator=user_translator, sleep_seconds=user_delay) for chunk in chunks]
# Save the translated text into a new PDF file
save_text_to_pdf(translated_chunks, output_pdf_path)

print(f"Translated PDF saved to {output_pdf_path}")
