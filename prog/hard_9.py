#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Составить UML-диаграмму деятельности, программу и произвести
# вычисление значения специальной функции по ее разложению в ряд
# с точностью e = 10^-10, аргумент функции вводится с клавиатуры.

import math
import sys

if __name__ == '__main__':
    x = float(input("Введите значение x: "))
    if (x<0) or (x>2):
        print("Illegal value of x", file=sys.stderr)
        exit(1)

    result = -x + 1
    k = 1
    EPS = 1e-10
    S = result
    while math.fabs(S) > EPS:
        S *= (-(x-1)*k**2)/((k+1)**2)
        result += S
        k += 1

    print("Вычисление с использованием разложения в ряд: ", result)