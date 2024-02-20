import csv
import os

pasta_csv = r'baseCarteira'
csv_unificado = []

for arquivo in os.listdir(pasta_csv):
    if arquivo.endswith('.csv'):
        caminho_arquivo = os.path.join(pasta_csv, arquivo)
        with open(caminho_arquivo, mode='r', encoding='utf-16') as arquivo_csv:
            ler_csv = csv.reader(arquivo_csv, delimiter='\t')  # Define o delimitador como tabulação
            csv_unificado.extend(list(ler_csv)[6:])  # Pula as primeiras 6 linhas

with open(r'C:\\Users\\vinicius.pereira\\Documents\\GitHub\\unificador-csv\\unificados\\Base_Minha_Carteira.csv', mode='w', newline='', encoding='utf-16') as csv_final:
    base = csv.writer(csv_final, delimiter='\t')  # Define o delimitador como tabulação
    for linha in csv_unificado:
        base.writerow(linha)