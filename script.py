import matplotlib.pyplot as plt
import numpy as np

h = 0.005

def ObjectiveFunction(x):
    result = np.exp(-x) - np.log(x) 
    return result

def Biseccion(a, b, lim):
    i = 0
    m = (a+b)/2
    while(i < lim):
        if(ObjectiveFunction(b)*ObjectiveFunction(m) < 0):
            a = m
        else:
            b = m
        m = (a+b)/2
        i = i+1
    return m

def FalsaPosicion(a, b, lim):
    i = 0
    m = a - (ObjectiveFunction(a)*(a-b))/(ObjectiveFunction(a)-ObjectiveFunction(b))
    while(i < lim):
        if(ObjectiveFunction(b)*ObjectiveFunction(m) < 0):
            a = m
        else:
            b = m
        m = a - (ObjectiveFunction(a)*(a-b))/(ObjectiveFunction(a)-ObjectiveFunction(b))
        i = i+1
    return m

def Newton(x0, lim):
    i = 0
    res = x0
    while(i<lim):
        res = res - ((h*ObjectiveFunction(res))/(ObjectiveFunction(res+h)-ObjectiveFunction(res)))
        i = i+1
    return res




print(Newton(2,10))
