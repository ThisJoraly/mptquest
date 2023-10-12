import sys
import time

import items
import missions


def inputarray(array):
    for i in array:
        print(i, end='; ')
def show_inv():
    print("Ваш инвентарь:")
    print(items.inventory)
def getinventoryitem():
    print(f"Доброе утро, день {missions.day}, сегодня вам необходимо идти на пары")
    print("Что вы возьмете на пары в этот прекрасный день? =)")
    # print(*items.home_items, sep="; ")
    print("1.ключи от хаты\n2.лопата\n3.ноутбук\n4.рюкзак с шмотками на физру\n5.телефон")
    try:
        taken = str(input("Перечислите номера вещей через \";\" (без пробелов у ;) ")) #пример: "1;2;3"
        # items.inventory = taken.split(";")
        my_keys_str = taken.split(";")
        my_keys_int= [int(string) for string in my_keys_str]  # создание списка целых значений
        items.inventory = [items.home_items2[key] for key in my_keys_int]
        checkKeys()
        show_inv()
    except ValueError:
        print("Неправильно введен выбор вещей")
        missions.badending("Нечисловой")

def checkKeys():
    if not("ключи от хаты" in items.inventory):
        print("Вы не взяли ключи от дома, вы не закрыли дверь, вашу хату обнесли, а вас сдали в детский дом. Игра окончена.")
        missions.badending("Обнесли...")

def printheart():
    print(" ██ ██ ")
    time.sleep(0.5)
    print("█▓▓█▓▒█")
    time.sleep(0.5)
    print("█▓▓▓▓▓█")
    time.sleep(0.5)
    print(" █▓▓▓█ ")
    time.sleep(0.5)
    print("  █▓█  ")
    time.sleep(0.5)
    print("   █   ")

def printmpt():
    # вывод ASCII-надписи "MPT"
    print("  __  __ _____ _______\n |  \/  |  __ \__   __|\n | \  / | |__) | | |   \n | |\/| |  ___/  | |   \n | |  | | |      | |   \n |_|  |_|_|      |_|   ")
def startnextday():
    missions.day += 1
    missions.startday()