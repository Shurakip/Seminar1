# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
def common_elements(n, m):
    set1 = set()
    set2 = set()

    # Вводим элементы первого множества
    print("Введите элементы первого множества:")
    for i in range(n):
        num = int(input())
        set1.add(num)

    # Вводим элементы второго множества
    print("Введите элементы второго множества:")
    for i in range(m):
        num = int(input())
        set2.add(num)

    # Находим общие элементы множеств
    common_elements = set1.intersection(set2)

    # Выводим результат
    print("Общие элементы:")
    for num in sorted(common_elements):print(num)
        
# Вводим количество элементов первого множества
n = int(input("Введите количество элементов первого множества: "))

# Вводим количество элементов второго множества
m = int(input("Введите количество элементов второго множества: "))

# Вызываем функцию для поиска общих элементов и выводим результат
common_elements(n, m)

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены 
# только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля 
# и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

N = int(input("Сколько кустов: "))
a = list(map(int, input(("Ягод на кустах (через пробел): ")).split()))

max_sum = 0
curr_sum = 0
for i in range(N-2):
    curr_sum = a[i] + a[i+1] + a[i+2]
    if curr_sum > max_sum:
        max_sum = curr_sum

print(max_sum, " ягод максимально можно собрать за один заход")