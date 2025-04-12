import copy
from sympy import *


def start():
    box = []
    i = 0
    while True:
        x = input(f"x_{i}: ")
        if x == "":
            answer = input("wanna break?Y/N: ")
            if answer == "Y":
                break
            continue
        try:
            float(x)
        except:
            print("try again!")
            continue
        y = input(f"y_{i}: ")
        if y == "":
            answer = input("wanna breake?Y/N: ")
            if answer == "Y":
                break
            continue
        try:
            float(y)
        except:
            print("try again!")
            continue
        box.append((float(x), float(y)))
        i += 1
    box = set(box)
    box = list(box)
    return box


def Lagranje_1():
    points = start()
    skip = 0
    x_numerator = []
    while skip < len(points):
        skip_x = points[skip][0]
        target_x = list()
        target_points = copy.deepcopy(points)
        target_points.remove(target_points[skip])
        for i in target_points:
            target_x.append(i[0])
        target_x.append(skip_x)
        target_x.append(points[skip][1])
        x_numerator.append(target_x)
        skip += 1
    return x_numerator


def Lagranje_2():
    A = Lagranje_1()
    x = symbols("x")
    eq_box = []
    for i in A:
        eq = []
        numerator = 1
        denumenator = 1
        for j in range(0, len(i)-2):
            numerator *= (x-(i[j]))
            denumenator *= (i[len(i)-2]-i[j])
        numerator *= i[len(i)-1]
        eq.append(numerator)
        eq.append(denumenator)
        eq_box.append(eq)
    return eq_box


def Lagranje_3():
    A = Lagranje_2()
    term = 0
    for i in A:
        term += ((i[0]/i[1]))
    clean = nsimplify(term, rational=True)
    print(pretty(simplify(clean)))


Lagranje_3()
