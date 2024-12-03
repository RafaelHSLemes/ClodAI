from setuptools import setup, find_packages

setup(
    name="ClodAI",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "torch",  # Adicione outras dependências aqui
        "sentencepiece",
        "FastAPI",
        "os-sys",
        "uvicorn",
        "regex",
        "nltk",
        "pdfplumber",
        "unicodedata2",
        "pandas",
        "scikit-learn",
        "collection"
    ],
    include_package_data=True,
    description="Modelo de IA especialista em empreendedorismo",
    author="Rafael H. S. Lemes",
    author_email="rafaelhslemes@gmail.com",
)