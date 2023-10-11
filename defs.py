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
    taken = str(input("Перечислите вещи через \";\" (без пробелов у ;) "))
    items.inventory = taken.split(";")
    show_inv()
    checkItems()
    checkKeys()

def checkKeys():
    if not("ключи от хаты" in items.inventory):
        print("Вы не взяли ключи от дома, вы не закрыли дверь, вашу хату обнесли, а вас сдали в детский дом. Игра окончена.")
        sys.exit(0)
def checkItems():
    if not("ключи от хаты" and "лопата" and "ноутбук" and "рюкзак со шмотками на физру" and "телефон" in items.inventory):
        print("Вы путаетесь в своих решениях, вы упали без сознания...")
        time.sleep(2)
        print("Дальше только ПУСТОТА.....")
        time.sleep(1)
        sys.exit(0)