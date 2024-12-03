import os

def listar_arquivos(diretorio, nivel=0):
    for item in os.listdir(diretorio):
        caminho = os.path.join(diretorio, item)
        if os.path.isdir(caminho):
            print(" " * nivel + f"[{item}]")  # Exibe a pasta
            listar_arquivos(caminho, nivel + 2)  # Chamada recursiva para subpastas
        elif item.endswith(".py"):
            print(" " * nivel + f"- {item}")  # Exibe os arquivos .py

# Substitua 'caminho_do_projeto' pelo caminho do seu projeto
caminho_do_projeto = "C:/Users/Usuario/Desktop/ClodAI/"
listar_arquivos(caminho_do_projeto)
