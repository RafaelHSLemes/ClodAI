import os
import re
import nltk
import pdfplumber
import unicodedata
import pandas as pd
from nltk.tokenize import sent_tokenize
from nltk.util import ngrams
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
nltk.download('punkt')
nltk.download('punkt_tab')

input_dir = 'C:/Users/Usuario/Desktop/ClodAI/books/'
pdf_files = [file for file in os.listdir(input_dir) if file.endswith('.pdf')]

def extract_text_from_pdf(pdf_path):
    text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + '\n'
    return text

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text

all_texts = []
for pdf_file in pdf_files:
    pdf_path = os.path.join(input_dir, pdf_file)
    text = extract_text_from_pdf(pdf_path)
    all_texts.append((pdf_file, text))

processed_texts = [(file, preprocess_text(text)) for file, text in all_texts]

def tokenize_sentences(text):
    return sent_tokenize(text)

tokenized_texts = [(file, tokenize_sentences(text)) for file, text in processed_texts]

output_dir = 'C:/Users/Usuario/Desktop/ClodAI/preprocess/preprocess_text/'

os.makedirs(output_dir, exist_ok=True)

for file, sentences in tokenized_texts:
    output_path = os.path.join(output_dir, f"{file.split('.')[0]}_processed.text")
    with open (output_path, 'w', encoding='utf-8') as f:
        for sentence in sentences:
            f.write(sentence + '\n')

combined_data = []
for _, sentences in tokenized_texts:
    combined_data.extend(sentences)

final_data_path = os.path.join(output_dir, 'final_training_data.txt')
with open(final_data_path, 'w', encoding='utf-8') as f:
    for sentence in combined_data:
        f.write(sentence + '\n')