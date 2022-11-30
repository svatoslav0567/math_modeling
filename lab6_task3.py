import matplotlib.pyplot as plt
import numpy as np

def ft3(a = 9, b = 5, title='slojno'):
    x = np.arange(-10, 10, 0.1)
    y = np.arange(-10, 10, 0.1)

    X, Y = np.meshgrid(x, y)
    fxy = (X ** 2 / a ** 2) + (Y ** 2 / b ** 2)-1

    plt.contour(X, Y, fxy, levels=[0])
    plt.axis('equal')
    plt.grid()
    plt.savefig('ellips.png')

ft3()   
