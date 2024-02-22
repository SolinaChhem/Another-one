Todo_list = []
while True:
    print("-" * 20)
    print("'q' => Quit the program")
    print("'1' => Add ToDo list")
    print("'2' => Remove ToDo list")
    print("'3' => Display ToDo list")
    user_input = input("Enter option: ")

    if user_input == "q":
        print("Bye Bye !")
        break

    elif user_input == "1":
        new_Todo_list = input("New ToDo list: ")
        Todo_list.append(new_Todo_list)

    elif user_input == "2":
        remove_Todo_list = input("Remove ToDo list: ")
        Todo_list.remove(remove_Todo_list)

    elif user_input == "3":
        for Todo in Todo_list:
            print(Todo_list)
