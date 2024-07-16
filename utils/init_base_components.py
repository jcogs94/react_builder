from utils.create_component import create_component

# Prompts user for wanting a "basic component structure added"
def init_base_components(source):
    init_components = False

    valid_input = False
    while not valid_input:
        user_input = input('Would you like to create a basic component structure (y/n)? ')

        if user_input.lower() == 'y':
            init_components = True
            valid_input = True
        if user_input.lower() == 'n':
            valid_input = True
        else:
            print('Invalid input. Please try again...\n')
    
    # If user responds 'y', creates Nav, Main, and Footer components
    if init_components:
        print('\nCreating structure...')
        create_component(source, "Nav")
        create_component(source, "MainComponent")
        create_component(source, "Footer")
        print('\nBasic structure built...')
