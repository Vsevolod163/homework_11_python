import math
import numpy as np
import matplotlib.pyplot as plt

# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

# Определить корни

# Найти интервалы, на которых функция возрастает

# Найти интервалы, на которых функция убывает

# Построить график

# Вычислить вершину

# Определить промежутки, на котором f > 0

# Определить промежутки, на котором f < 0

def func(x):
    y = (-12*x**4)*math.sin(math.cos(x)) - 18*x**3+5*x**2 + 10*x - 30
    return y

def y_list(x_list):
    y_list = []
    for x in x_list:
        y_list.append(func(x))
    return y_list

all_x = np.arange(-200, 200, 0.1)
all_y = y_list(all_x)

def solution(all_x, all_y):
    plt.grid()
    plt.plot(all_x, all_y)
    for i in range(1, len(all_y)):
        if all_y[i-1] > all_y[i]:
            plt.plot(all_x[i-1], all_y[i-1], 'r.')
            plt.plot(all_x[i], all_y[i], 'r.')
    for i in range(1, len(all_y)):
        if all_y[i-1] < all_y[i]:
            plt.plot(all_x[i-1], all_y[i-1], 'g.')
            plt.plot(all_x[i], all_y[i], 'g.')
    plt.title(f'Т.к. функция тригонометрическая, у неё бесконечно много корней. Корнями являются значения X на тех участках графика, где Y == 0.')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')

    plt.show()

solution(all_x, all_y)