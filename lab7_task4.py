from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ball, = plt.plot([], [], '|', color='r', label='Ball')

x0 = 0.1
y0 = 0.1
C = 0.3
D = 0.33
frames = 100
edge = 1
x = []
y = []

for n in range(frames):
    xn = x0 ** 2 - y0 ** 2 + C
    yn = 2 * x0 * y0 + D

    x.append(xn)
    y.append(yn)

    x0 = xn
    y0 = yn
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
def animate(i):
    ball.set_data(x[:i], y[:i])

ani = FuncAnimation(fig, animate, frames=100, interval=30)
ani.save('fractal.gif')