import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
butterfly, = plt.plot([], [], '|', color='g', label='Batterfly')
'''
def func(t):
    x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) + np.sin(t / 12) ** 5)
    y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) + np.sin(t / 12) ** 5)
    return x, y
'''
def func(t):
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 *t)
    return x, y

ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
plt.axis('equal')
x = []
y = []
def animate(i):
    x.append(func(t=i)[0])
    y.append(func(t=i)[1])
    butterfly.set_data(x, y)
    
ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 2 * np.pi, 0.01), interval=30)
                             

ani.save('heart.gif')
