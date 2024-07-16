def get_index_lines(source):
    root = source.replace('/src/components', '')
    directories = root.split('/')
    name = directories[(len(directories) - 1)]
    
    print(name)

get_index_lines('/home/jcogs/code/sandbox/python_scripts_testing/src/components')
