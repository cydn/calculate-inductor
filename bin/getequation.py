def getK(P1 : tuple, P2: tuple, x: float):
    '''
    give it two points and it returns
    the equation.
    '''
    k = (P2[1]-P1[1])/(P2[0]-P1[0])
    b = P1[1]-k*P1[0]
    # ret = '%.5fx+%.5f' % (k,b)
    return k*x+b


if __name__ == '__main__':
    x = 0.15
    print(getK((0.2,0.92),(0.1,0.96), x))