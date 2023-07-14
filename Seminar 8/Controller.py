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
        elif num == 5:
            print("Выход из программы...")
            break
main()