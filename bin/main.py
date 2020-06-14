from math import pi
from .getequation import getK

def getL(R: float, l: float):
    
    S = pi*R**2
    u = 4*pi*10**(-7)
    N = l/(0.49*10**(-3))

    c = 2*R/l 

    if c <= 0.1:
        k = getK((0,1), (0.1,0.96), c)
    elif c <= 0.2:
        k = getK((0.2,0.92), (0.1,0.96), c)
    elif c <= 0.3:
        k = getK((0.2,0.92), (0.3,0.88), c)
    elif c <= 0.4:
        k = getK((0.3,0.88), (0.4,0.85), c)
    elif c <= 0.6:
        k = getK((0.4,0.85), (0.6,0.79), c)
    elif c <= 0.8:
        k = getK((0.8,0.74), (0.6,0.79), c)
    elif c <= 1.0:
        k = getK((0.8,0.74), (1.0,0.69), c)
    elif c <= 1.5:
        k = getK((1.0,0.69), (1.5,0.60), c)
    elif c <= 2.0:
        k = getK((1.5,0.60), (2.0,0.52), c)
    elif c <= 3.0:
        k = getK((3.0,0.43), (2.0,0.52), c)
    elif c <= 4.0:
        k = getK((4.0,0.37), (3.0,0.43), c)
    elif c <= 5.0:
        k = getK((4.0,0.37), (5.0,0.32), c)
    elif c <= 10:
        k = getK((10,0.20), (5.0,0.32), c)
    elif c <= 20:
        k = getK((10,0.20), (20,0.12), c)

    L = k*u*N**2*S/l 
    return L