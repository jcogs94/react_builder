from utils.create_env import create_env
from utils.create_services_dir import create_services_dir
from utils.init_base_components import init_base_components
from utils.adjust_init_files import adjust_init_files

# Asks user if new project, prompts for init changes if true
def new_project(source):
    is_new_project = False
    
    valid_input = False
    while not valid_input:
        user_input = input('\nIs this a new project (y/n)? ')

        if user_input.lower() == 'y':
            is_new_project = True
            valid_input = True
        elif user_input.lower() == 'n':
            valid_input = True
        else:
            print('Invalid input. Please try again...')

    # If new project, runs other prompts for init changes
    if is_new_project:
        create_env(source)
        create_services_dir(source)
        base_was_init = init_base_components(source)
        adjust_init_files(source, base_was_init)
