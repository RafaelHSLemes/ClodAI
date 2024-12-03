# -*- coding: utf-8 -*-
from src.inference.pipeline import tokenize, detokenize  # ajuste o import conforme seu código

# Teste manual
text = "Teste de tokenização"
tokens = tokenize(text)
detokenized_text = detokenize(tokens)

print(f"Texto original: {text}")
print(f"Tokens gerados: {tokens}")
print(f"Texto reconstruído: {detokenized_text}")