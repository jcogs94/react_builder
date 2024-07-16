import os
from utils.create_component import create_component

def build_components(source):
    print('\n===========================')
    print('==== COMPONENT BUILDER ====')
    print('===========================')
    
    building = False
    valid_input = False

    # Verifies user would like to build components
    while not valid_input:
        user_input = input('\nWould you like to start building components (y/n)? ')

        if user_input.lower() == 'y':
            building = True
            valid_input = True
        elif user_input.lower() == 'n':
            valid_input = True
        else:
            print('Invalid input. Please try again...')

    # If user wants to build components, loops through "building" components until user exits
    while building:
        root = '' + str(source)

        is_nested = False
        valid_input = False

        # Checks if user would like to nest the new component inside a current one
        while not valid_input:
            user_input = input('\nWould you like this component nested inside another component (y/n)? ')
            if user_input.lower() == 'y':
                is_nested = True
                valid_input = True
            elif user_input.lower() == 'n':
                valid_input = True
            else:
                print('Invalid input. Please try again...')
        
        # If the use wants to nest the new component, prompts user to input the nested directory structure
        # and verifies that the existing component exists
        if is_nested:
            valid_input = False
            while not valid_input:
                new_root = input('Please enter the relative path for the parent component from the "components" directory: ')
                if os.path.exists(os.path.join(root, new_root)):
                    root = os.path.join(root, new_root)
                    valid_input = True
                    print()
                else:
                    print('Invalid input. Please try again...\n')
        
        # Prompts user for the new component's name and creates it
        component_name = input('Please enter the name of the new component: ')
        create_component(root, component_name)

        # Prompts user to either continue or exit
        valid_input = False
        while not valid_input:
            keep_building = input('\nWould you like to build another component (y/n)? ')
            if keep_building.lower() == 'y':
                valid_input = True
            elif keep_building.lower() == 'n':
                valid_input = True
                building = False
            else:
                print('Invalid input. Please try again...\n')
