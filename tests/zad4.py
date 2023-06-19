import random
import math


def kak(deisv):
    a=eval(deisv)
    return(f'{a}')
def zad44():
    deisv=input("""Введите действие(a+b,a-b,a*b,a/b,a**b,math.factorial(a),math.fabs(a),random.randint(a, b),math.acos(a))
    или конец для завершения работы """)
    while deisv!="конец":
        print(kak(deisv))
        deisv=input("""Введите действие(a+b,a-b,a*b,a/b,a**b,math.factorial(a),math.fabs(a),random.randint(a, b),math.acos(a))
        или конец для завершения работы """)