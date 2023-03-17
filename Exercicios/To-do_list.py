import os
import json
from datetime import datetime

to_do_list = []
undo = []
redo = []

def is_command(command):
    commands = ['list', 'undo', 'redo']
    if command in commands:
        return True
    return False

def is_action(action):
    if action == 'clear':

        os.system('clear')
        return True

    elif action == 'exit':
        exit(0)

    elif action == 'save list':

        current_time = datetime.now()
        formated_time = current_time.strftime('%H:%M:%S')

        file_path = f'/home/luan/workspace/PythonProject/Exercicios/to_do_list_{formated_time}.json'
        with open(file_path, 'w') as file:
            json.dump(to_do_list, file, indent=2)

        return True


while True:

    print("Comands: list, undo, redo.")
    print('Actions: clear, exit, save list')
    task_or_command = input("Enter a task or a command: ")

    if is_command(task_or_command):

        if task_or_command == 'list':

            print(*to_do_list, sep='\n')

        elif task_or_command == 'undo':
            if undo:

                undoing = undo.pop()

                to_do_list.remove(undoing)
                print(*to_do_list, sep='\n')
                print()

                redo.append(undoing)

            else:

                print('Nothing to undo')
                print(*to_do_list, sep='\n')
                print()

        elif task_or_command == 'redo':

            if redo:
                redoing = redo.pop()

                to_do_list.append(redoing)
                print(*to_do_list, sep='\n')
                print()

                undo.append(redoing)

            else:
                print('Nothing to redo')
                print(*to_do_list, sep='\n')

    else:

        if not is_action(task_or_command):
            to_do_list.append(task_or_command)
            undo.append(task_or_command)
            print(*to_do_list, sep='\n')
            print()
