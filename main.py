import os
from translate import Translate
from retranslate import Retranslate

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
        print("\n___----------- M E N U -----------___")
        print("-|                                 |-")
        print("-|  1 ->  E n c o d e              |-")
        print("-|                                 |-")
        print("-|  2 ->  D e c o d e              |-")
        print("-|                                 |-")
        print("-|  3 <-  E x i t                  |-")                  
        print("-|_________________________________|-")

if __name__ == "__main__":
    while True:
        clear_screen()

        menu()

        choix = input("\nsaise votre choix: ")

        if choix == "1":
            clear_screen()
            text = input("\nEnter a text: ").lower()
            print(f"\ntext encode : \n< {Translate(text)} >\n")
            input()
        elif choix == "2":
            clear_screen()
            text = input("\nEnter a code: ")
            print(f"\n--> \" {Retranslate(text)} \"\n")
            input()
        elif choix == "3":
            clear_screen()
            print("\n\nGoodbye!\n\n")
            break
