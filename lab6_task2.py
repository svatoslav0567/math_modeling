import matplotlib.pyplot as plt
import numpy as np

def ft2(k = 1, title='genadi_gorin'):
    x1 = np.arange(0.1, 10, 0.1)
    y1 = k / x1

    x2 = np.arange(-10, -0.1, 0.1)
    y2 = k / x2


    plt.plot(x1, y1, x2, y2, label ='giperbola')  
    plt.axis('equal')
    plt.grid()
    plt.savefig('giperbola.png')
    

ft2()