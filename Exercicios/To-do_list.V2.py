# Modification of code To-do_list.py

import os
import json
from datetime import datetime

to_do_list = []
list_undo = []
list_redo = []

def print_list():
    print('TASKS: ')
    for item in to_do_list:
        print(f'\t{item}')


def undo():
    if list_undo:

        undoing = list_undo.pop()
        to_do_list.remove(undoing)

        print_list()
        print()

        list_redo.append(undoing)
    else:

        print('Nothing to undo\n')
        print_list()
        print()

def redo():
    if list_redo:

        redoing = list_redo.pop()
        to_do_list.append(redoing)

        print_list()
        print()

        list_undo.append(redoing)

    else:

        print('Nothing to redo\n')
        print_list()
        print()


def is_command(command):
    commands = ['list', 'undo', 'redo']

    if command in commands:

        if command == 'list':
            print_list()
        elif command == 'undo':
            undo()
        elif command == 'redo':
            redo()

    else:
        if not is_action(task_or_command):
            to_do_list.append(task_or_command)
            list_undo.append(task_or_command)
            print_list()
            print()


def is_action(action):
    if action == 'clear':

        os.system('clear')
        return True

    elif action == 'exit':
        exit(0)

    elif action == 'save list':

        current_time = datetime.now()
        formated_time = current_time.strftime("%d%m%Y")
        file_path = f"/home/luan/workspace/PythonProject/Exercicios/to_do_list_{formated_time}.json"

        with open(file_path, 'w') as file:
            json.dump(to_do_list, file, indent=2)

        return True

while True:

    print("Comands: list, undo, redo.")
    print('Actions: clear, exit, save list.')
    task_or_command = input("Enter a task or a command: ")
    print()

    is_command(task_or_command)
