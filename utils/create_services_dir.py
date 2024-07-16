import os

# Creates a "services" directory if the user inputs 'y'
def create_services_dir(source):
    create = False
    
    valid_input = False
    while not valid_input:
        user_input = input('Would you like to create a services directory (y/n)? ')

        if user_input.lower() == 'y':
            create = True
            valid_input = True
        elif user_input.lower() == 'n':
            valid_input = True
        else:
            print('Invalid input. Please try again...')

    if create:
        services_path = source.replace('/components', '/services')
        
        # Creates directory only if it does not already exist
        if os.path.exists(services_path):
            print('\nservices directory already exists...\n')
        else:
            os.mkdir(services_path)
            print('\nservices directory created...\n')
