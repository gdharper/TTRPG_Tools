#! /usr/bin/python3

import platform
import subprocess

def init_alt_buffer():
    print('\033[?1049h\033[H')

def exit_alt_buffer():
    print('\033[?1049l')

def clear_buffer():
    _=subprocess.run("cls" if platform.system() == "Windows" else "clear", shell = True)

########################################################################################
# Main Program Loop
########################################################################################
if __name__ == "__main__":
    init_alt_buffer()

    turnCount = 0
    exit = False
    while not exit:
        clear_buffer()
        print(f'Turn {turnCount + 1}')
        print()
        print('Enter Command')
        print('\tExit        : exit to shell, erasing current encounter state.')
        print()

        command = input(': ').lower()

        if command == "exit":
            exit = True

    exit_alt_buffer()
    
