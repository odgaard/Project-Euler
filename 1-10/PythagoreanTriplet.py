__author__ = 'Jacob'
from math import sqrt
#c=sqrt((a**2)+(b**2))
#1000=a+b+sqrt((a**2)+(b**2))
#a=1000-b-sqrt((a**2)+(b**2))
#a**2 = 1000**2 - b**2 - (a**2) - b**2
#2* a**2= 1000**2 - 2*b**2
#a=sqrt((1000**2 - 2*b**2)/2)

def findB():
    for b in range(0,100000):
        a=sqrt((1000**2 - 2*b**2)/2)
        c=sqrt((a**2)+(b**2))
        if (a**2)+(b**2)==(c**2):
            if a+b+c==1000:
                print(b)
findB()


