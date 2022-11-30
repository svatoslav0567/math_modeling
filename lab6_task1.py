import matplotlib.pyplot as plt
import numpy as np

def ft1(x, y):
    plt.plot(x, y, label ='square')  
    plt.savefig('square.png')
    plt.axis('equal')

ft1([1, 1, 5, 5, 1], [1, 5, 5, 1, 1])