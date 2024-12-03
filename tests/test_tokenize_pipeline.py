# -*- coding: utf-8 -*-
import sys
import os
import pytest

# Adiciona o diretório raiz do projeto ao sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from src.inference.pipeline import tokenize, detokenize

@pytest.mark.parametrize(
    "input_text",
    [
        "Teste de tokenização",
        "Outro exemplo",
        "Um texto mais longo para testar",
        "Texto com caracteres especiais: çãô",
        "1234567890",
    ]
)
def test_tokenize_and_detokenize(input_text):
    """Testa se o texto original é recuperado após tokenizar e detokenizar"""
    tokens = tokenize(input_text)  # Aplica tokenização
    recovered_text = detokenize(tokens)  # Reverte os tokens para texto
    assert recovered_text == input_text, f"Esperado '{input_text}', mas obteve '{recovered_text}'"