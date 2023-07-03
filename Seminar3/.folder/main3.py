# Сдвиг элементов на k...
# def shift_sequence(sequence, k):
#     if k <= 0:
#         print("Ошибка: K должно быть положительным числом.")
#         return
    
#     n = len(sequence)
#     k = k % n  # Убедимся, что сдвиг будет циклическим
    
#     res = sequence[-k:] + sequence[:-k]  # Выполняем сдвиг элементов вправо
    
#     return res
    
# # Пример использования функции
# input_sequence = [1, 2, 3, 4, 5]
# k = 2
# output_sequence = shift_sequence(input_sequence, k)
# print(output_sequence)

# Напишите программу для печати всех уникальных 
# значений в словаре. 
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII 
# ":" S007 "}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# dictionary_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
#                    {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, 
#                    {" VIII ":"S007"}]
                   
# unique_values = set()  # Создаем пустое множество для уникальных значений

# values_list = []  # Создаем пустой список для всех значений в словарях
# for dictionary in dictionary_list:
#     values_list.extend(dictionary.values())  # Добавляем все значения из текущего словаря в список

# unique_values = set(values_list)  # Преобразуем список во множество, чтобы оставить только уникальные значения

# print(unique_values)  # Выводим результат

