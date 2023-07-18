from Database import *
from View import *

def main():
    while True:
        num = input_num()
        if num == 1:
            info = input_info()
            write_info(info)
        elif num == 2:
            char = input_char()
            find_info(char)
        elif num == 3:
            dell = input_dell()
            found = find_dell(dell)
            if found:
                print("Пользователь успешно удален.")
            else:
                print("Пользователь не найден")
        elif num == 4:
            edit = input_edit()
            new_info = input_info()
            found = edit_info(edit, new_info)
            if found:
                print("Информация о пользователе успешно изменена.")
            else:
                print("Пользователь не найден.")
        elif num == 5:
            print("Выход из программы...")
            break
main()