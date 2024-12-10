 ## Graphic interface 
from matplotlib import pyplot as plt


plt.style.use('Solarize_Light2')

eixo_x_dias = [1,2,4,5,7,9]
eixo_y_temperaturas = [33, 24, 30, 26, 28, 30]
eixo_y_minimas = [20,21,15,16,17,18]


plt.plot(eixo_x_dias, eixo_y_temperaturas)
plt.plot(eixo_x_dias, eixo_y_minimas)

plt.title('Clima tempo')
plt.legend(['Tep.Max', 'Tem.Min'])

plt.show()

