
__author__ = 'Дьякова Елизавета Сергеевна'

# Задача-1: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользоваться данным ресурсом можно только с 18 лет"
age = int(input("Введите Ваш возраст "))
if age >= 18:
	print("Доступ разрешен")
else:
	print("Извините, пользоваться данным ресурсом можно только с 18 лет")

# Задача-2: Напишите программу, которая спрашивает "Четные или нечетные?", в зависимости от ответа,
# используя цикл с предусловием while или for in
# вывести в одну строку через пробел соотвествующие числа от 0 до 20
# Пример работы:
# $ "Четные или нечетные?"
# четные
# 0 2 4 6 8 10 12 14 16 18 20
# $ "Четные или нечетные?"
# нечетные
# 1 3 5 7 9 11 13 15 17 19
# $ "Четные или нечетные?"
# qwerty (или любая другая строка)
# Я не понимаю, что вы от меня хотите...

#цикл for
i = 1
chet = str("четные")
nechet = str("нечетные")
a = input("Четные или нечетные?")
if a == chet:
    for i in range(1, 21):
        if i % 2 == 0:
            print(i)
elif a == nechet:
    for i in range(1, 21):
        if i % 2 != 0:
            print(i)
else:
    print("Я не понимаю чего вы от меня хотите..")


#цикл while
i = 1
chet = str("четные")
nechet = str("нечетные")
a = input("Четные или нечетные?")
if a == chet:
    while i <= 20:
        if i % 2 == 0:
            print(i)
        i += 1
elif a == nechet:
    while i <= 20:
        if i % 2 != 0:
            print(i)
        i += 1
else:
    print("Я не понимаю чего вы от меня хотите..")

# Задача-3: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

#1 решение
a = int(input("Введите число a "))
m = a % 10
a = a // 10
while a > 0:
    if a % 10 > m:
        m = a % 10
    a = a // 10
print(m)



#2 решение
a = input('Введите число ')
print(max(a))
