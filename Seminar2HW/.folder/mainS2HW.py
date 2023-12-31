# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
def min_number_of_flips(coins):
    k = coins.count('H') # 'H' - герб
    n = len(coins)
    flips = min(k, n - k)
    return flips

coins = ['H', 'H', 'H', 'H', 'T', 'T', 'T', 'H', 'T']
print(min_number_of_flips(coins)) 

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
def guess_numbers(s, p):
    for x in range(1, 1001): # перебираем возможные значения X от 1 до 1000
        for y in range(1, 1001): # перебираем возможные значения Y от 1 до 1000
            if x + y == s and x * y == p: # проверяем условие суммы и произведения
                return (x, y) # возвращаем найденную пару чисел X и Y
    return None # если не найдено подходящих чисел, возвращаем None

s = 37 # сумма, задуманная Петей
p = 336 # произведение, задуманное Петей
result = guess_numbers(s, p)
if result is not None:
    x, y = result
    print(f"Числа X и Y, задуманные Петей: {x} и {y}")
else:
    print("Подходящие числа X и Y не найдены")
    
    # Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
def print_powers_of_two(N):
    power = 0  # текущая степень двойки
    result = 1  # текущее значение степени двойки

    # пока текущая степень двойки не превышает число N
    while result <= N:
        print(result)
        power += 1
        result = 2 ** power

# вызов функции с указанным числом N
print_powers_of_two(200)