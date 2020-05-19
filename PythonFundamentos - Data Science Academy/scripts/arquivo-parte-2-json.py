# Manipulando Arquivos JSON (Java Script Object Notation)
import json
# Criando um dicionário
dict = {'nome': 'Guido van Rossum',
        'linguagem': 'Python',
        'similar': ['c','Modula-3','lisp'],
        'users': 1000000}

for k,v in dict.items():
    print(k,v)

# Convertendo dicionário
print(json.dumps(dict))

# Criando um arquivo Json
with open('arquivos/dados.json', 'w') as arq:
    arq.write(json.dumps(dict))

# Leitura de arquivos Json
with open('arquivos/dados.json', 'r') as arq:
    texto = arq.read()
    data = json.loads(texto)

print(data['nome'])

# Imprimindo um arquivo Json copiado da internet
from urllib.request import urlopen

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
data = json.loads(response)[0]
print('Título: ', data['title'])
print('URL: ', data['url'])
print('Duração: ', data['duration'])
print('Número de Visualizações: ', data['stats_number_of_plays'])

# Copiando o conteúdo de um arquivo para o outro
import os

arquivo_fonte = 'arquivos/dados.json'
arquivo_destino = 'arquivos/json_data.txt'

# Método 1
with open(arquivo_fonte, 'r') as infile:
    text = infile.read()
    with open(arquivo_destino, 'w') as outfile:
        outfile.write(text)

# Método 2
open(arquivo_destino, 'w').write(open(arquivo_fonte, 'r').read())

# Leitura de arquivos Json
with open('arquivos/json_data.txt', 'r') as arq:
    texto = arq.read()
    data = json.loads(texto)

print(data)
