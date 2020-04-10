# Manipulanto TXT
import os

texto = "Cientista de Dados é a profissão que mais tem crescido em todo mundo.\n"
texto = texto + "Esses profissionais precisam se especializar em Programação, Estatística e Machine Learning.\n"
texto += "E claro, em Big Data."
print(texto)

# Criando arquivo
arq = open(os.path.join('arquivos/cientista.txt'), 'w')

#Gravando
for palavra in texto.split():
    arq.write(palavra + ' ')

arq.close()

# Lendo o arquivo
arq = open('arquivos/cientista.txt', 'r')
conteudo = arq.read()
arq.close()

print(conteudo)

print('Usando a expressão with - método close automático')
# Usando a expressão with - método close automático
with open('arquivos/cientista.txt', 'r') as arq:
    conteudo = arq.read()

print(len(conteudo))