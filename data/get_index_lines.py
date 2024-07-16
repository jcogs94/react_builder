def get_index_lines(source):
    root = source.replace('/src/components', '')
    directories = root.split('/')
    name = directories[(len(directories) - 1)]
    
    if '_' and '-' in name:
        name = name.replace('_', ' ')
    elif '_' in name:
        name = name.replace('_', ' ')
    elif '-' in name:
        name = name.replace('-', ' ')

    name = name.title()

    index = [
        '<!doctype html>\n',
        '<html lang="en">\n',
        '<head>\n',
        '    <meta charset="UTF-8" />\n',
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0" />\n',
        ('    <title>' + name + '</title>\n'),
        '</head>\n',
        '<body>\n',
        '    <div id="root"></div>\n',
        '    <script type="module" src="/src/main.jsx"></script>\n',
        '</body>\n',
        '</html>\n',
    ]

    return index
