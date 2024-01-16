#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Найти координаты точки пересечения прямых заданных уравнениями 
# a1x + b1y + c1 =0 и a2x + b2y + c2 =0, 
# либо сообщить совпадают, параллельны или не существуют.

if __name__ == '__main__':
    A1, B1, C1 = map(float, input('Введите A1, B1, C1 через пробел: ').split())
    A2, B2, C2 = map(float, input('Введите A2, B2, C2 через пробел: ').split())

if ((A1 == 0) and (B1 == 0)) or ((A2 == 0) and (B2 == 0)):
    print('прямые не существуют')
else:
    if (A1 * B2 == A2 * B1) and (A1 * C2 == A2 * C1):
        print('прямые совпадают')
    elif A1 * B2 == A2 * B1:
        print('прямые параллельны')
    else:
        X = (C1 * B2 - C2 * B1) / (B1 * A2 - B2 * A1)
        Y = (C2 * A1 - C1 * A2) / (B1 * A2 - B2 * A1)
        print(f'X = {X:.2f}, Y = {Y:.2f}')
