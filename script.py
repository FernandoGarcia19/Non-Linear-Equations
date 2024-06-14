import matplotlib.pyplot as plt
import numpy as np
import os
import msvcrt
h = 0.005
ACCURACY = 1000

def ObjectiveFunction(x):
    result = np.exp(-x) - np.log(x) 
    return result

def Biseccion(a, b, lim):
    if(ObjectiveFunction(a)*ObjectiveFunction(b) < 0):
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
    else:
        return "No root"

def FalsaPosicion(a, b, lim):
    if(ObjectiveFunction(a)*ObjectiveFunction(b) < 0):
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
    else:
        return "No root"

def Newton(x0, lim):
    i = 0
    res = x0
    while(i<lim):
        res = res - ((h*ObjectiveFunction(res))/(ObjectiveFunction(res+h)-ObjectiveFunction(res)))
        i = i+1
    return res


def MainMenu():
    ans = ""
    while(ans != "0"):
        print("NON-LINEAR-EQUATION-SOLVER: MAIN MENU")
        print("1. Biseccion")
        print("2. Falsa Posicion")
        print("3. Newton")
        print("0. Salir")
        ans = input("Opcion: ")
        match ans:
            case "1":
                a = int(input("a:"))
                b = int(input("b:"))
                print(Biseccion(a,b,ACCURACY))
            case "2":
                a = int(input("a:"))
                b = int(input("b:"))
                print(FalsaPosicion(a,b,ACCURACY))
            case "3":
                x0 = int(input("x0:"))
                print(Newton(x0, ACCURACY))
            case "0":
                print("Hasta pronto!")
            case _:
                print("Opcion no valida")
        input()
        os.system("cls")
    
MainMenu()
