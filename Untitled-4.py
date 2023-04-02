import random
import math
def factorial(o):
    if o==0:
        return 1
    else:
        return o*factorial(o-1)

deisv=input("Введите символ операции(+,-,*,/,^,!,|,random,arcos)")
if deisv=="+":
    a=int(input("Введите первое слагаемое "))
    b=int(input("Введите второе слагаемое "))
    print("Сумма равна = ",a+b)
elif deisv=="-":
    a=int(input("Введите уменьшаемое "))
    b=int(input("Введите ввычитаемое "))
    print("Разность равна = ",a-b)
elif deisv=="*":
    a=int(input("Введите первый множитель "))
    b=int(input("Введите второй множитель "))
    print("Произведение равно = ",a*b)
elif deisv=="/":
    a=int(input("Введите делимое "))
    b=int(input("Введите делитель "))
    print("Частное равно = ",a/b)
elif deisv=="^":
    a=int(input("Введите основание степени "))
    b=int(input("Введите показатель степени "))
    print("Степень равна = ",a**b)
elif deisv=="|":
    a=int(input("Введите число "))
    print("Модуль равен = ",abs(a))
elif deisv=="!":
    a=int(input("Введите число "))
    print("Факториал равен = ",factorial(a))
elif deisv=="random":
    a=int(input("Введите нижнюю границу диапазона "))
    b=int(input("Введите верхнюю границу диапазона "))
    print("Число = ",random.randint(a, b))
elif deisv=="arcos":
    a=float(input("Введите число "))
    print("Арккосинус = ", math.acos(a))
else:
    print("Ошибка!!!")