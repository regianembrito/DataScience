# Manipulação de Arquivos em Python

# Nome do arquivo vem por input
filename = input("Digite o nome do arquivo: ")
filename = "arquivos/" + filename + ".txt"
arq = open(filename, "w")
arq.write("Incluindo o texto com atenção")
arq.close()

# Abrindo arquivo para leitura
arq = open(filename, "r")
print(arq.read())
arq.close()