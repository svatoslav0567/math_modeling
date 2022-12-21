from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ball, = plt.plot([], [], '.', color='r', label='Ball')
tr, = plt.plot([], [], '-', color='r')
weels, = plt.plot([], [], '-', color='b')


ax.set_xlim(-2, 15)
ax.set_ylim(0, 10)
plt.axis('equal')
R = 1
frames = np.arange(0, 4.85 * np.pi, 0.1)

def cycloid(R, t):
    x = R * (t - np.sin(t))
    y = R *(1 - np.cos(t))
    return x, y

def weeelsf(R, x0, y0, vx0, vy0, t):
    x0 = x0 + vx0 * t
    y0 = y0 + vy0  * t

    alpha = np.arange(0, 2 * np.pi, 0.1)
    x = x0 + R * np.cos(alpha)
    y = y0 + R * np.sin(alpha)
    return x, y

X, Y = [], []

def animate(i):
   X.append(cycloid(R=R, t =i)[0])
   Y.append(cycloid(R=R, t =i)[1])

   ball.set_data(cycloid(R = R, t =i))
   tr.set_data(X, Y)

   weels.set_data(weeelsf(R, 0, R, 1, 0, t =i))

ani = FuncAnimation(fig, animate, frames=frames, interval=30)
ani.save('ball.gif')