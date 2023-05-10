import csv

# Defina o caminho do arquivo de entrada (txt)
caminho_arquivo = 'C:\\Users\\victor.viana.CAPITAL\\Desktop\\Nova pasta\\arquivo.txt'

# Defina o caminho do arquivo de saída (csv)
caminho_saida = 'C:\\Users\\victor.viana.CAPITAL\\Desktop\\Nova pasta\\arquivo.csv'

# Abra o arquivo de entrada no modo leitura
with open(caminho_arquivo, 'r') as arquivo_txt:
    # Leia as linhas do arquivo de texto
    linhas = arquivo_txt.readlines()

# Abra o arquivo de saída no modo escrita
with open(caminho_saida, 'w', newline='') as arquivo_csv:
    # Crie o escritor CSV
    escritor_csv = csv.writer(arquivo_csv)

    # Escreva as linhas no arquivo CSV
    for linha in linhas:
        # Separe os valores da linha usando o caractere de separação adequado
        valores = linha.strip().split(';')  # Substitua ';' pelo separador correto

