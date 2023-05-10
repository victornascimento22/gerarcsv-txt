import csv

# Defina o caminho do arquivo de entrada (txt)
caminho_arquivo = 'data/AEAE.txt'

# Defina o caminho do arquivo de saída (csv)
caminho_saida = 'ae2.csv'

# Lista para armazenar as colunas
colunas = []
# Lista para armazenar os valores das colunas
valores = []

# Abra o arquivo de entrada no modo leitura
with open(caminho_arquivo, 'r') as arquivo_txt:
    # Leia as linhas do arquivo de texto
    linhas = arquivo_txt.readlines()

# Organize os dados em colunas
for linha in linhas:
    partes = linha.strip().split(' - ')
    coluna = partes[0]
    valores_coluna = partes[1].split(', ')
    colunas.append(coluna)
    valores.append(valores_coluna)

# Obtenha o número máximo de valores em uma coluna
max_valores = max(len(vals) for vals in valores)

# Preencha os valores ausentes com espaços em branco
valores_preenchidos = [vals + [''] * (max_valores - len(vals)) for vals in valores]

# Transpõe a lista de valores para obter os valores em colunas distintas
valores_transpostos = list(map(list, zip(*valores_preenchidos)))

# Abra o arquivo de saída no modo escrita
with open(caminho_saida, 'w', newline='') as arquivo_csv:
    # Crie o escritor CSV
    escritor_csv = csv.writer(arquivo_csv)

    # Escreva os cabeçalhos
    escritor_csv.writerow(colunas)

    # Escreva os valores em colunas distintas
    for linha_valores in valores_transpostos:
        escritor_csv.writerow(linha_valores)

print("Arquivo CSV criado com sucesso!")
