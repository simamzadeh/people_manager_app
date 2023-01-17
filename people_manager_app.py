import pandas as pd
pd.set_option('display.width', 400)
pd.set_option('display.max_columns',10)

database = pd.read_csv("employee_database.csv")

print(database)

menu_options = {
    1: 'Create new record.',
    2: 'Edit existing record.',
    3: 'Delete record.',
    4: 'Display full details of existing record.',
    5: 'Exit menu.'
}

def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


option = int(input('Enter option number: '))


def option1():
    print('Handle option \'Option 1\'')


def option2():
    print('Handle option \'Option 2\'')


def option3():
    print('Handle option \'Option 3\'')


def option4():
    print('Handle option \'Option 4\'')



while(True):
    print_menu()

    option = int(input('Enter option number: '))

    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 3:
        option3()
    elif option == 4:
        option4()
    elif option == 5:
        print('Thanks message before exiting')
        exit()
    else:
        print('Invalid option. Please enter a number between 1 and 5.')



