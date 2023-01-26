def choice_todo():
    print("\n Доступные операции с телефонной книгой:\n\
    1 - импорт;\n\
    2 - экспорт;\n\
    3 - сортировка по id;\n\
    4 - сортировка по имени.\n\
    Для выхода нажмите любую другую цифру.\n")
    ch = int (input("Введите цифру: "))
    return ch

def input_data():
    id = int(input("Введите id записи: "))
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    brith_name = input("Введите дату рождения: ")
    phone_number = int(input("Введите номер контакта: "))
    data = (f"{id}, {last_name}, {first_name}, {middle_name}, {brith_name}, {phone_number}\n")
    with open("Phonebook.txt","a+") as file:
        file.write(data)

def print_data():
    with open("Phonebook.txt","r") as file:
        for i in file.readlines():
            print(i,end="")

def sort_ID():
    with open("Phonebook.txt","r+") as file:
        data = file.readlines()
        new_data = []
        for line in data:
            temp = line.split(",")
            new_data.append(temp)
        new_data = sorted(new_data,key = lambda x:x[0])
        file.seek(0)
        for i in new_data:
            file.write(",".join(i))
    print("Успешно отсортированно по id")

def sort_Name():
    with open("Phonebook.txt","r+") as file:
        data = file.readlines()
        new_data = []
        for line in data:
            temp = line.split(",")
            new_data.append(temp)
        new_data = sorted(new_data,key = lambda x:x[1])
        file.seek(0)
        for i in new_data:
            file.write(",".join(i))
    print("Успешно отсортированно по имени")