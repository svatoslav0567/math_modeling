from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
star, = plt.plot([], [], '.', color='r', label='Star')


t = np.arange(0, 4*np.pi, 0.1)
x = 12 * np.cos(t) + 8 * np.cos(1.5 * t)
y = 12 * np.sin(t) + 8 * np.sin(1.5 * t)

ax.set_xlim(-25, 25)
ax.set_ylim(-25, 25)
plt.axis('equal')
def animate(alpha):
    alpha = np.arange(0, 2 * np.pi, 0.1)
    X = x * np.cos(alpha) - y * np.sin(alpha)
    Y = y * np.cos(alpha) + x * np.sin(alpha)
    star.set_data(X, Y)

ani = FuncAnimation(fig, animate, frames=np.arange(0, 4 * np.pi, 0.1), interval=30)

ani.save('star.gif')