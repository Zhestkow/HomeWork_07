from view import choice_todo, input_data, print_data, sort_Name, sort_ID
def start():
    while True:
        ch = choice_todo()
        if ch == 1:
            input_data()
        elif ch == 2:
            print_data()
        elif ch == 3:
            sort_ID()
        elif ch == 4:
            sort_Name()
        else:
            print ("Вы вышли из программы!")
            break
            