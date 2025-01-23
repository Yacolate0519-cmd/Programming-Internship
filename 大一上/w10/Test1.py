def mean():
    print('1. Add new student id and name')
    print('2. Update student name')
    print('3. Delete student')
    print('4. show all students')
    print('0. Quit')

data = {}

while True:
    mean()
    choice = int(input("Input the move: "))
    if 0 <= choice <= 4:
        if choice == 0:
            break
        elif choice == 1:
            id , name = input("Enter the new student id and name(use ; to seperate): ").split(';')
            data[id] = name
        elif choice == 2:
            id , newName = input("Enter the new student id and name(use ; to seperate): ").split(';')
            data[id] = newName
        elif choice == 3:
            id = input("Enter student id: ")
            del data[id]
        elif choice == 4:
            # print(f'ID{:12s}Name{'Name':20s}')
            print('--'*30)
            for id , name in data.items():
                print(f'{id:12s}{name:20s}')
            print()
        else:
            print("Invalid error")