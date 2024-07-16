import os
from utils.create_component import create_component

def build_components(source):
    # Loops through main "building" of components until user exits
    building = True
    while building:
        temp_source = '' + str(source)
        
        valid_input = False
        while not valid_input:
            is_subcomponent = input('\nWould you like this component nested inside another component (y/n)? ')
            if is_subcomponent.lower() == 'y':
                while not valid_input:
                    new_parent = input('Please enter the relative path for the parent component from the "components" directory: ')
                    if os.path.exists(os.path.join(temp_source, new_parent)):
                        temp_source = os.path.join(temp_source, new_parent)
                        valid_input = True
                        print()
                    else:
                        print('Invalid input. Please try again...\n')
            elif is_subcomponent.lower() == 'n':
                valid_input = True
            else:
                print('Invalid input. Please try again...')
        
        component_name = input('Please enter the name of the new component: ')
        create_component(temp_source, component_name)

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
