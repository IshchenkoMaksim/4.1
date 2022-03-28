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
        self.second = float(input("Введите второе число диапазона: "))

    def display(self):
        print(f"Число принадлежит диапазону [{self.first}, {self.second}):")

    def rangecheck(self, x):
        return self.first <= x < self.second


def make_rangecheck(first, second):
    if type(first) and type(second) != float and type(first) and type(second) != int:
        raise ValueError()
    else:
        return InRange(first, second)


if __name__ == "__main__":
    in_range = InRange()
    m = make_rangecheck(10, 100)
    m.display()
    print(m.rangecheck(16))
