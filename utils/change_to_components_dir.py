import os

def change_to_components_dir(source):
    if os.path.exists(os.path.join(source, 'src')):
        source = os.path.join(source, 'src')
    elif os.path.exists(os.path.join(source, 'frontend', 'src')):
        source = os.path.join(source, 'frontend', 'src')
    else:
        source = os.path.join(source, 'src')
        os.mkdir(source)
    
    source = os.path.join(source, 'components')
    if not os.path.exists(source):
        os.mkdir(source)
    
    return source
