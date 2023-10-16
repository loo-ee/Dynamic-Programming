from colorama import Fore
from util.util import custom_print, colored_array_print
from caesar_cipher import caesar_cipher


def main():
    choice: int

    while True:
        getting_input = True
        print_menu()

        while getting_input:
            try:
                choice = int(input('Enter choice: '))
            except:
                print("Enter a valid input...")
                continue

            if choice in range(7):
                getting_input = False

        match choice:
            case 0:
                break

            case 1:
                caesar_cipher.run()


def print_menu():
    print('\n*********************************************************************')
    colored_array_print("GREEDY ALGORITHMS", Fore.GREEN, False) 

    print('''

    [0] Exit
    [1] Caesar Cipher
    ''')


if __name__ == '__main__':
    main()
