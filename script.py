import matplotlib.pyplot as plt
import numpy as np

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

print(Biseccion(1,2,5))