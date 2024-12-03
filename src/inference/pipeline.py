# -*- coding: utf-8 -*-
import sentencepiece as spm
import sys
import os
from setuptools import setup, find_packages

# Adiciona o diretório raiz ao sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from model.entrepreneurGPT import model
import torch

sp = spm.SentencePieceProcessor(model_file='C:/Users/Usuario/Desktop/ClodAI/src/inference/tokenizer.model')
def tokenize(text):
    tokens = sp.encode(text, out_type=int)
    print(f"Texto: '{text}' → Tokens: {tokens}")  # Diagnóstico
    return tokens

def detokenize(tokens):
    text = sp.decode(tokens)
    print(f"Tokens: {tokens} → Texto: '{text}'")  # Diagnóstico
    return text

def generate_response(input_text):
    model.eval()
    tokens = tokenize(input_text)
    input_tensor = torch.tensor(tokens).unsqueeze(0)
    output_tokens = model.generate(input_tensor)
    return detokenize(output_tokens.squeeze(0).tolist())

if __name__ == "__main__":
    setup(
        setup(
            name="ClodAI",
            version="0.1",
            packages=find_packages(),
        )
    )