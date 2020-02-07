'''
Run this file to run console 
'''
from time import sleep
from os import system
import consolecases
import consolestrings as strings
import consoleconfig as ccng 
from funcmap import construct_funcmap, print_funcmap
from consolecommon import clear_screen
from consoledecorator import case_decorator

def logo_title(title: str):
    '''Prints logo title'''
    print("{:-^40s}".format(title))

def show_cases(funcmap: dict):
    '''Prints function map prettily'''
    logo_title(strings.LOGO_TITLE)
    print_funcmap(funcmap)

def enter_prompt():
    '''Prints enter prompt message and than returns input()'''
    print(strings.ENTER_PROMPT, end=' ')
    return input()

def exit_program():
    '''
    Exit program
    '''
    print(strings.EXIT_MSG)
    sleep(ccng.MSG_WAIT_TIME)
    clear_screen()
    exit()

def main_interface():
    '''
    Main function for console interface
    '''
    print(strings.START_MSG)
    funcmap = construct_funcmap(consolecases, [exit_program], case_decorator)
    
    run = 1
    try:
        while run:
            clear_screen()
            show_cases(funcmap)

            # Get key to func map
            command = enter_prompt()  

            # Pressing enter without specifying input exits program
            if not command:
                clear_screen()
                exit_program()

            clear_screen()
            if command in funcmap:
                funcmap[command][1]()
            else:
                print(strings.INVALID_TERMINAL_INPUT_MSG)
                sleep(ccng.MSG_WAIT_TIME)

    except KeyboardInterrupt:
        # Ensures proper exit when Kbinterrupt
        exit_program()

if __name__ == '__main__':
    main_interface()
    