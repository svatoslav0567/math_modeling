import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

fig, ax = plt.subplots()
bullet, = plt.plot([], [], 'o', color='r', label='Ball')
wall, = plt.plot([20, 20], [30, -110], '-', color='brown')

ax.set_xlim(-30, 30)
ax.set_ylim(-100, 30)
frames = np.arange(0, 10 * np.pi, 0.1)

def bullet_function(C, q, d, a, B, x0, y0, vx0, vy0, t, m, Proch):
    v = np.sqrt(vx0 ** 2 + vy0 ** 2)
    Ek = m * v ** 2 / 2-

    x = x0 + vx0 * t
    y = y0 + vy0 * t

    b = (C * q * d ** 2 * a ** -1) * math.log(1 + B * v ** 2)

    if x >= 20:
        if Ek > Proch:
            x = x0 + vx0 * t
            y = y0 + vy0 * t
        if  Ek == Proch: 
            x = 21
            y = y0
        if Ek < Proch:
            x = 20
            y = y0

    if t == 0.1 and Ek > Proch:
        print(b)      
    return x, y
    

def animate(i):
    bullet.set_data(bullet_function(C=245, q=5, d=0.5, a=1, B=25.5, x0=-30, y0=-10, vx0=10, vy0=0, t=i, m=5, Proch=5))

ani = FuncAnimation(fig, animate, frames = frames, interval = 30)

ani.save('project.gif')