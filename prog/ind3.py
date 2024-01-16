#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Если к сумме цифр двузначного числа прибавить квадрат этой суммы, то снова получится
# это двузначное число. Найти все эти числа.

print_numbers = []
if __name__ == '__main__':
    for number in range(10, 100):
        digit_one = number // 10  # Получаем первую цифру
        digit_two = number % 10  # Получаем вторую цифру
        digit_sum = digit_one + digit_two  # сумма цифр
        squared_sum = digit_sum * digit_sum  # Возводим сумму в квадрат
        if number == (digit_sum + squared_sum):
            print_numbers.append(number)

print("Все двузначные числа, удовлетворяющие условию:", print_numbers)