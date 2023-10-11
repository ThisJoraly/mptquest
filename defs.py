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
    print(*items.home_items, sep="; ")
    taken = str(input("Перечислите вещи через \";\" (без пробелов у ;) ")) #пример: "ключи от хаты;рюкзак с шмотками на физру
    items.inventory = taken.split(";")
    show_inv()
    checkKeys()

def checkKeys():
    if not("ключи от хаты" in items.inventory):
        print("Вы не взяли ключи от дома, вы не закрыли дверь, вашу хату обнесли, а вас сдали в детский дом. Игра окончена.")
        sys.exit(0)

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