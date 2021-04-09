from os import system, name
import re
from lib.node import Node
from lib.linked_list import LinkedList


# variable whether to display the list in reverse or not
display_reverse = False


# define our clear function
def clear():
    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def main_menu():
    display_list()
    print("+++++++++++++++++++++++++++++++++")
    print("1. Create New List")
    print("2. Insert")
    print("3. Delete")
    print("4. Find")
    print("5. Display")
    print("6. Exit")
    print("+++++++++++++++++++++++++++++++++")


def display_list():
    if list is not None and not list.is_empty():
        list.print_list(display_reverse)
        print("")


def get_memu_choice():
    to_return = None
    while True:
        to_return = input("Enter your choice: ")
        if re.match("^[1-6]$", to_return):
            break
        else:
            print("Please enter a number between 1 ~ 6")
    return int(to_return)


def get_head_or_tail():
    to_return = None
    while True:
        to_return = input("To the head or tail? (h/t): ")
        if to_return == "h" or to_return == "t":
            break
        clear()
        print("Please enter either h or t")
    clear()
    return to_return


def get_head_tail_or_data():
    to_return = None
    while True:
        to_return = input("Delete head, tail or data? (h/t/d): ")
        if to_return == "h" or to_return == "t" or to_return == "d":
            break
        clear()
        print("Please enter either h, t or d")
    clear()
    return to_return


def get_max_or_min():
    to_return = None
    while True:
        to_return = input("Find max or min? (+/-): ")
        if to_return == "+" or to_return == "-" or to_return == "d":
            break
        clear()
        print("Please enter either + (for max) or - (for min)")
    clear()
    return to_return


def add_to_list(head_or_tail):
    item = int(input("Enter number to add to the list: "))
    if head_or_tail == "h":
        list.prepend(item)
    elif head_or_tail == "t":
        list.append(item)
    clear()


def delete_from_list(head_tail_or_data):
    if head_tail_or_data == "h":
        list.pop_left()
    elif head_tail_or_data == "t":
        list.pop()
    elif head_tail_or_data == "d":
        item = int(input("Enter number to delete from the list: "))
        list.delete(item)  # not working!!!
    clear()


def find_from_list(max_or_min):
    value = None
    if max_or_min == "+":
        value = list.max()
        print("Maximum value = ", value)
    elif max_or_min == "-":
        value = list.min()
        print("Minimum value = ", value)


def change_display_order():
    global display_reverse
    current = "Normal"
    if display_reverse:
        current = "Reverse"
    print("Current Order: ", current)
    user_input = None
    while True:
        user_input = input("Switch order? (y/n): ")
        if user_input == "y" or user_input == "n":
            break
        clear()
        print("Please enter either y or n")
    display_reverse = not display_reverse
    clear()


list = None
clear()
while True:
    main_menu()
    choice = get_memu_choice()
    clear()

    if choice == 1:
        list = LinkedList()
        print("The linked list has been created.")
    elif choice == 2:  # insert
        if list is None:
            print("Please create a linked-list first")
            continue

        # choose head or tail
        display_list()
        head_or_tail = get_head_or_tail()

        # add to the list
        display_list()
        add_to_list(head_or_tail)

    elif choice == 3:  # delete
        if list is None:
            print("Please create a linked-list first")
            continue

        # choose head, tail or data
        display_list()
        head_tail_or_data = get_head_tail_or_data()

        # delete from the list
        display_list()
        try:
            delete_from_list(head_tail_or_data)
        except:
            print("Number not found")

    elif choice == 4:  # find
        if list is None:
            print("Please create a linked-list first")
            continue

        # max, min
        display_list()
        max_or_min = get_max_or_min()

        # find max or min
        find_from_list(max_or_min)

    elif choice == 5:  # display
        if list is None:
            print("Please create a linked-list first")
            continue

        # foward or backward
        display_list()
        change_display_order()

    else:
        main_menu()
        break
