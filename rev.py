import os

def listar_arquivos_pastas():
    itens = os.listdir(".")
    
    for item in itens:
        print(item)

listar_arquivos_pastas()
