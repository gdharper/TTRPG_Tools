#! /usr/bin/python3

import platform
import random
import subprocess

########################################################################################
# CLI Buffer Control Routines
########################################################################################

def init_alt_buffer(): print('\033[?1049h\033[H')

def exit_alt_buffer(): print('\033[?1049l')

def clear_buffer(): _=subprocess.run("cls" if platform.system() == "Windows" else "clear", shell = True)


########################################################################################
# Utility Functions
########################################################################################

def d(n : int): return random.randint(1,n) if n > 0 else 0

def int_or_zero(string : str):
    try:
        return int(string)
    except:
        return 0

def read_pos_int(prompt : str): return max(0, int_or_zero(input(prompt))) 

def read_int(prompt : str): return int_or_zero(input(prompt))

########################################################################################
# Combatant Class Definition
########################################################################################

class Combatant:
    def __init__(self, name : str, faction : str, initMod : int, maxhp : int, ac : int):
        self.name = name
        self.faction = faction
        self.initMod = initMod
        self.init = max(1, d(20) + self.initMod)
        self.maxhp = maxhp
        self.hp = maxhp
        self.ac = ac

    def __str__(self):
        s = f'{self.name} ({self.faction})\n' \
        f'Initiative: {self.init} (+{self.initMod})\n' \
        f'HP: {self.hp}/{self.maxhp}\n' \
        f'Armor Class: {self.ac}\n'
        return s

    def __eq__(self, other):
        return self.init == other.init and self.initMod == other.initMod and self.faction == other.faction and self.name == other.name
    
    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return ((self.init < other.init) or
                (self.init == other.init and self.initMod < other.initMod) or
                (self.init == other.init and self.initMod == other.initMod and self.faction < other.faction) or
                (self.init == other.init and self.initMod == other.initMod and self.faction == other.faction and self.name < other.name))

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not slef.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)


########################################################################################
# Core Functions
########################################################################################

def display_turn_info(completedTurns : int, combatants : list):
    print(f'Turn {completedTurns + 1}')
    print()
    for c in combatants:
        print (f'{c.name} ({c.faction}) - {c.init} : {c.hp}/{c.maxhp}')

    print()

def read_command():
    print('Enter Command')
    print('\tExit       : exit to shell, erasing current encounter state.')
    print('\tRoll       : roll a die')
    print('\tAdd        : add a new combatant to the encounter.')
    print('\tImport     : import a set of combatants from a csv file.')
    print()
    return input(': ').lower()

def create_combatant():
    name = input('New combatant name: ')
    faction = input('New combatant faction: ')
    
    while not (init := read_int('New combatant initiative modifier: ')):
        pass
    while not (hp := read_pos_int('New combatant max hp: ')):
        pass
    while not (ac := read_pos_int('New combatant armor class: ')):
        pass

    return Combatant(name,faction,init,hp,ac)

########################################################################################
# Main Program Loop
########################################################################################
if __name__ == "__main__":
    init_alt_buffer()
    turnCount = 0
    combatants = []
    exit = False
    while not exit:
        display_turn_info(turnCount, sorted(combatants))

        command = read_command()

        if command == 'exit' or command == 'quit':
            exit = True
        elif command[:4] == 'roll':
            print()
            if val := int_or_zero(command[4:]):
                print(d(val))
            else:
                print(d(read_pos_int('Sides: ')))
            print()
            input('Press enter to continue')
        elif command == 'add':
                combatant = create_combatant()
                print()
                print(combatant)
                print()
                input('Press enter to continue')
                combatants.append(combatant)

        clear_buffer()

    exit_alt_buffer()
    
