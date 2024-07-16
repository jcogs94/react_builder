from utils.adjust_init_vite import adjust_init_vite

def adjust_init_files(source):
    adjust_init = False
    
    valid_input = False
    while not valid_input:
        user_input = input('Would you like to adjust the basic install files (y/n)? ')

        if user_input.lower() == 'y':
            adjust_init = True
            valid_input = True
        elif user_input.lower() == 'n':
            valid_input = True
        else:
            print('Invalid input. Please try again...\n')
    
    if adjust_init:
        valid_input = False
        while not valid_input:
            user_input = input('Did you use "vite" or "create-react-app"? ')
            if user_input.lower() == 'vite':
                adjust_init_vite(source)
                valid_input = True
            elif user_input.lower() == 'create-react-app':
                print('This feature is currently unavailable.\n')
                valid_input = True
            else:
                print('Invalid input. Please try again...\n')
