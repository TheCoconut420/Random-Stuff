from cmath import sqrt
import fractions
import math
x = 0
xn=x

def rechnung(x, xn):
    while abs(xn-x) > 0.0001:
        f = 1/x + x**4 - 1
        f_ableitung = -1/x**2 + 4*x**3
        xn =x
        x = x - f/f_ableitung
        print(x)

rechnung(float(input("Geben Sie eine Zahl ein: ")), float(x + 1))