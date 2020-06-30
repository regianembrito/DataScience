'''
Matplotlib
Construindo Plots
'''

import matplotlib as mpl
mpl.__version__

'''O matplotlib.pyplot é uma coleção de funções e estilos que fazem com que o Matplotlib funcione 
como o Matlab.'''
import matplotlib.pyplot as plt

'''O método plot() define os eixos do gráfico'''
plt.plot([1, 3, 5], [2, 5, 7])
plt.show()

x = [1, 4, 5]
y = [3, 7, 2]

plt.plot(x, y)
plt.xlabel('Variável 1')
plt.ylabel('Variável 2')
plt.title('Teste Plot')
plt.show()

'''Gráficos em Barras'''
x = [2,4,6,8,10]
y = [6,7,8,2,4]
plt.bar(x, y, label='Barras', color='r')
plt.legend()
plt.show()

x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]
plt.bar(x, y, label='Barras1', color='r')
plt.bar(x2, y2, label='Barras2', color='y')
plt.legend()
plt.show()