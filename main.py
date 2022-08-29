from matplotlib import pyplot as plt
import numpy as np

valores_produto_A =  [6,7,8,4,4]
valores_produto_B =  [3,12,5,4.4,6]

x1 = np.arange(len(valores_produto_A))
x2 = [x+0.25 for x in x1]


plt.bar(x1, valores_produto_A, width=0.25, label = 'Produto Azul', color ='deepskyblue')
plt.bar(x2, valores_produto_B, width=0.25, label = 'Produto Verde', color ='mediumseagreen')

meses = ['Agosto','Setembro','Outubro','Novembro','Dezembro']
plt.xticks([x + 0.25 for x in range(len(valores_produto_A))],meses)

plt.legend()

plt.title("Vendas Mensal")
plt.show()
