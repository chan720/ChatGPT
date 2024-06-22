import docx
import openai
import PyPDF2
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
# Pdf file extractor
def pdf_reader(file_path):
    with open(file_path,'rb') as file:
        reader=PyPDF2.PdfReader(file)
        # print("Reading PDF file")
        text=''
        for page in reader.pages:
            text +=page.extract_text()
        return text

# docx file extractor
def  doc_reader(file_path):
    doc = docx.Document(file_path)
    text=''
    for paragraph in doc.paragraphs:
        text +=paragraph
    return text
# txt file extractor
def text_reader(file_path):
    with open(file_path,'r') as file:
        text=file.read()
    return text
# Check the file to which it belongs
def extract_text(file_path):
    if file_path.endswith('.pdf'):
        pdf_reader(file_path)
    elif file_path.endswith('.docx'):
        doc_reader(file_path)
    elif file_path.endswith('.txt'):
        text_reader(file_path)
    else:
        print("wrong path!")

#enter your API Key
openai.api_key='Your API-KEY'
def process_text(text):
    completion=openai.ChatCompletion.create(
        model="GPT-3.5 Turbo",
        messages=[{
            "role": "user",
            "content": f"Please Detect the following Language and convert it into precise English?  text is: {text}"

        }]
    )
    return completion.choices[0].message.content.strip()
# Calling the methods
text=extract_text('faisal.pdf') 
print(process_text(text))
