def write_info(info):
    with open("data.txt", "a", encoding="utf-8") as file:
        file.write(info)
    
def find_info(char):
    with open("data.txt", "r", encoding="utf-8") as file:
        lst = file.readlines()
        count = 0
        for line in lst:
            if char in line: 
                count += 1
                print(f"{count}) {line.strip()}")