import csv

with open('arquivos/numeros.csv', 'w') as arqu:
    writer = csv.writer(arqu)
    writer.writerow(('primeira', 'segunda', 'terceira'))
    writer.writerow((55,93,76))
    writer.writerow((62,14,86))

with open('arquivos/numeros.csv', 'r', encoding='utf8', newline='\r\n') as arq:
    leitor = csv.reader(arq)
    for x in leitor:
        print('Número de colunas', len(x))
        print(x)
