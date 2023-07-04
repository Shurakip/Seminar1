# N = int(input("Введите количество элементов в первом массиве: "))
# array1 = []
# for i in range(N):
#     num = int(input("Введите элемент первого массива: "))
#     array1.append(num)

# M = int(input("Введите количество элементов во втором массиве: "))
# array2 = []
# for i in range(M):
#     num = int(input("Введите элемент второго массива: "))
#     array2.append(num)

# result = []
# for num in array1:
#     if num not in array2:
#         result.append(num)

# print("Элементы первого массива, которых нет во втором массиве:")
# for num in result:
#     print(num, end=" ")
    
    
    
    
    
    
    
#     Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве 
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# n = int(input("Колич. элем. в массиве "))
# arr = []
# count = 0

# for i in range(n):
#     arr.append(int(input()))
    
# for i in range(1, n-1):
#     if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
#         count += 1
        
# print(count)


def sum_of_divisors(n):
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum

k = int(input("Введите число k: "))

for n in range(1, k+1):
    m = sum_of_divisors(n)
    if m <= k and sum_of_divisors(m) == n and n < m:
        print(n, m)