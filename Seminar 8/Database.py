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
                
def find_dell(dell):
    with open("data.txt", "r", encoding="utf-8") as file:
        lst = file.readlines()
    found = False
    with open("data.txt", "w", encoding="utf-8") as file:
        for line in lst:
            if dell not in line:
                file.write(line)
            else:
                found = True
    return found

def edit_info(info, new_info):
    with open("data.txt", "r", encoding="utf-8") as file:
        lst = file.readlines()
    found = False
    with open("data.txt", "w", encoding="utf-8") as file:
        for line in lst:
            if info in line:
                file.write(new_info)
                found = True
            else:
                file.write(line)
    return found