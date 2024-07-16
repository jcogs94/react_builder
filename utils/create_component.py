import os

# Creates component files base on input source and name
def create_component(source, component_name):
    print('\nCreating ' + component_name + ' component...')
    
    # Creates new directory for component if it does not already exist
    component_directory_path = os.path.join(source, component_name)
    if not os.path.exists(component_directory_path):
        os.mkdir(component_directory_path)
        print(component_name + ' directory created...')
    else:
        print(component_name + ' directory already exists...')

    # Paths for new jsx and css files
    jsx_path = os.path.join(component_directory_path, (component_name + '.jsx'))
    css_path = os.path.join(component_directory_path, (component_name + '.css'))
    
    # Checks if file exists and will only create the file if not
    if os.path.exists(jsx_path):
        print(component_name + '.jsx already exists...')
    else:
        # Creates new jsx file and writes boilerplate code
        jsx_f = open(jsx_path, 'w')
        jsx_f.writelines([
            ("import './" + component_name + ".css'\n\n"),
            ("const " + component_name + " = () => {\n"),
            "    return <>\n", "        \n", "    </>\n", "}\n\n",
            ("export default " + component_name + "\n")
        ])

        jsx_f.close()
        print(component_name + '.jsx created...')

    # Checks if file exists and will only create the file if not
    if os.path.exists(css_path):
        print(component_name + '.css already exists...')
    else:
        # Creates empty css file
        css_f = open(css_path, 'w')

        css_f.close()
        print(component_name + '.css created...')

    print('Done')
