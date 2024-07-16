import os

# Prompts user for source and returns valid input
def get_source():
    source = ''
    valid_source = False

    # Loop input prompt until user inputs valid source path
    while not valid_source:
        source = input("Please enter the exact path for the project's main directory: ")
        valid_source = os.path.exists(source)

        if valid_source:
            print('Source valid...')
            return source
        else:
            print('Source invalid... Please try again...\n')
