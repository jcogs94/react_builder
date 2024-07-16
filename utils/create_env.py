import os

# Prompts user for if need to create .env, if true, creates
def create_env(source):
    create = False
    
    valid_input = False
    while not valid_input:
        user_input = input('Would you like to create a .env file (y/n)? ')

        if user_input.lower() == 'y':
            create = True
            valid_input = True
        elif user_input.lower() == 'n':
            valid_input = True
        else:
            print('Invalid input. Please try again...\n')
    
    # If user responds 'y', creates .env in root dir and adds .env to .gitignore
    if create:
        root = source.replace('/src/components', '')
        env_path = os.path.join(root, '.env')

        env = open(env_path, 'w')
        env.close()

        if os.path.exists(os.path.join(root, '.gitignore')):
            git_ignore_path = os.path.join(root, '.gitignore')
            git_ignore = open(git_ignore_path, 'a')
            git_ignore.write("\n.env\n")
        
        print('\n.env created and added to .gitignore...\n')
