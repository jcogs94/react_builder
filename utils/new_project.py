from utils.create_env import create_env
from utils.adjust_init_files import adjust_init_files
from utils.init_base_components import init_base_components

def new_project(source):
    is_new_project = False
    
    valid_input = False
    while not valid_input:
        user_input = input('\nIs this a new project (y/n)? ')

        if user_input.lower() == 'y' or user_input.lower() == 'n':
            is_new_project = True
            valid_input = True
        else:
            print('Invalid input. Please try again...')

    if is_new_project:
        create_env(source)
        adjust_init_files(source)
        init_base_components(source)
