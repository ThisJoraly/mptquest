import csv
import sys
import time
import json
import items
import missions
import os

clear = "\n" * 100


def stats():
    pass
1

def menu():
    printmpt()
    print("ТРОЛЛЬ - КВЕСТ: ВЫЖИТЬ В МПТ ЗА 5 ДНЕЙ")
    print("Ваша цель не получить 2 + сделать так чтобы ты за эту неделю остался сухим. Удачи")
    print("Вы - парень, учащийся на втором курсе.")
    print("Выберите действие:\n\t1.Начать игру\n\t2.Статистика")
    c = int(input("> "))
    if c == 1:
        print(clear)
        getinventoryitem()
        missions.startday()
    elif c == 2:
        print(clear)
        stats()

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
        my_keys_int = [int(string) for string in my_keys_str]  # создание списка целых значений
        items.inventory = [items.home_items2[key] for key in my_keys_int]
        checkKeys()
        show_inv()
    except ValueError:
        print("Неправильно введен выбор вещей")
        missions.badending("Нечисловой")

def add_ending(dict, name, file_name):
    data = read_json_file("file.json")
    dict[name] = 1
    write_json_file(file_name, dict)
def write_json_file(file_name, dict):
    javason = json.dumps(dict, ensure_ascii=False)

    with open(file_name, "w", encoding="utf-8") as my_file:
        my_file.write(javason)
def read_json_file(file_name):
    with open(file_name, 'r', encoding="utf-8") as file:
        data = json.load(file)
    return data

def dict_to_csv2(file_name, dict):
   with open(file_name, 'w') as f:  # You will need 'wb' mode in Python 2.x
       w = csv.DictWriter(f, dict.keys())
       w.writeheader()
       w.writerow(dict)
def dict_to_csv(file_name, dict):
   with open(file_name, 'w', newline='') as file:
       writer = csv.DictWriter(file, fieldnames=dict[0].keys())
       writer.writeheader()
       writer.writerows(dict)

def json_to_csv(json_name, csv_name):
   dict = read_json_file(json_name)
   dict_to_csv(csv_name, dict)

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

