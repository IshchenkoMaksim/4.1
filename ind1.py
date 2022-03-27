#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Поле first — целое число, левая граница диапазона, включается в
диапазон; поле second — целое число, правая граница диапазона,
не включается в диапазон. Пара чисел представляет полуоткрытый
интервал [first, second). Реализовать метод rangecheck() —
проверку заданного целого числа на принадлежность диапазону
"""


class InRange:

    def __init__(self, first=0, second=0):
        self.first = first
        self.second = second

    def read(self):
        self.first = float(input("Введите первое число диапазона: "))
        self.second = int(input("Введите второе число диапазона: "))

    def display(self):
        if rangecheck(self):
            print("Число принадлежит диапазону")
        else:
            print("Число не принадлежит диапазону")


def rangecheck(self):
    x = float(input("Введите число: "))
    return self.first <= x < self.second


if __name__ == "__main__":
    in_range = InRange()
    in_range.read()
    in_range.display()
