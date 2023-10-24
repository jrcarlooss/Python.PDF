import PyPDF2
import os

# Diretório contendo os arquivos PDF a serem combinados
diretorio = [
   
    r'c:\ \ \    .pdf',
    r'c:\ \ \   .pdf',
    r'c:\ \ \   .pdf',
    r'c:\ \ \   .pdf',
    r'c:\ \ \   .pdf',
    r'c:\ \ \   .pdf'
    
]

   

# Nome do arquivo de saída
arquivo_saida = r'caminho-do-arquivo-para-armazenagem'


# Criar um objeto PDF para a saída
pdf_saida = PyPDF2.PdfMerger()

# Iterar sobre a lista de arquivos e adicionar todos os PDFs ao objeto PDF de saída
for arquivo in diretorio:
    pdf_saida.append(arquivo)

# Salvar o arquivo de saída com a extensão .pdf e o nome correto
with open(arquivo_saida, 'wb') as f:
    pdf_saida.write(f)

# Agora você tem um único arquivo "arquivos_combinados.pdf" com todos os PDFs no diretório.
