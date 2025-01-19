import matplotlib.pyplot as plt
import sympy as sp
import numpy as np


x = sp.symbols('x')
#я не знаю какую функцию делать, так что взял девятую:) но можно ее поменять
f = (x - 5)**2 * sp.cos(x**2 - 7)
# вывод обычного графика
F = sp.lambdify(x, f, 'numpy')
plt.figure(figsize=(10, 5))
plt.title("График 1")
Ox = np.linspace(-10, 10, 1000)
Oy = F(Ox)
plt.plot(Ox, Oy, color='blue')

#максимальное и минимальное значение на интервале
dict = [[F(x), x] for x in Ox]
MY = [max(dict), min(dict)]
plt.scatter([MY[0][1], MY[1][1]],[MY[0][0], MY[1][0]], color='red', s=50)

#Косательная и нормаль к точке на 1 графике
def TNG(x0):
    f_x0 = F(x0)
    f_derivative = sp.diff(f, x) #запись производной
    F_derivative = sp.lambdify(x, f_derivative, 'numpy')  # функция от неё
    f_deff_x0 = F_derivative(x0)
    tangent = f_x0 + f_deff_x0 * (x - x0)
    Tangent = sp.lambdify(x, tangent, 'numpy')
    Oy = Tangent(Ox)
    plt.plot(Ox, Oy, "--", color='g')
TNG(2) # можно поменять абсциссу точки касания


def NRML(x0):
    # нормаль не получается корректно отрисовать и я искренне не понимаю почему....
    f_x0 = F(x0)
    f_derivative = sp.diff(f, x)
    F_derivative = sp.lambdify(x, f_derivative, 'numpy')  # функция от неё
    f_deff_x0 = F_derivative(x0)
    normal = f_x0 - ((1 / f_deff_x0) * (x - x0))
    print(normal)
    #print(normal)
    Normal = sp.lambdify(x, normal, 'numpy')
    #print(Normal)
    Oy = Normal(Ox)
    plt.plot(Ox, Oy, "-.", color='r')
NRML(2)

# вывод 1 производной
f_derivative = sp.diff(f, x) #производная
F_derivative = sp.lambdify(x, f_derivative, 'numpy') #функция
Ox = np.linspace(-10, 10, 1000)
Oy = F_derivative(Ox)
plt.figure(figsize=(10, 5))
plt.title("График 2")
plt.plot(Ox, Oy, color='green')

# вывод 2 производной
plt.figure(figsize=(10, 5))
plt.title("График 3")
f_second_derivative = sp.diff(f_derivative, x)
F_second_derivative = sp.lambdify(x, f_second_derivative, 'numpy')
Ox = np.linspace(-10, 10, 1000)
Oy = F_second_derivative(Ox)
plt.plot(Ox, Oy, color='r')

#Касательное расслоение
fig, ax = plt.subplots(figsize=(10, 5))  # Размер области графика (ширина, высота)
ax.set_xlim(-2.5, 7)  # взял самый адекватный участок
ax.set_ylim(-250, 250)
plt.title("График 4")
Ox = np.linspace(-10, 10, 1000)
Oy = F(Ox)
plt.plot(Ox, Oy, color='blue')
x0 = np.linspace(-2.5, 7, 10) # можно поменять только абсциссу точки касания
for i in x0:
    TNG(i)





plt.show()