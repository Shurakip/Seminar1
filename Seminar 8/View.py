def input_num():
    ask = int(input("1 - Добавить пользователя\n2 -Найти пользователя\n5 - Выйти "))
    return ask

def input_info():
    fio = input("Введи ФИО человека - ")
    birth = input("Введи дату рождения - ")
    tele = input("Введи номер тел - ")
    info = f"{fio},{birth},{tele}\n"
    return info

def input_char():
    char = input("Введите искомые данные - ")
    return char