import os
from data.lint_lines import lint_lines
from data.main_lines import main_lines
from data.get_index_lines import get_index_lines


# "Cleans" up default Vite files
def adjust_init_vite(source):
    root = source.replace('/src/components', '')

    print('\nAdjusting vite install...')

    # Adds lines to lint
    lint_path = os.path.join(root, '.eslintrc.cjs')
    lint = open(lint_path, 'w')
    lint.writelines(lint_lines)
    lint.close()
    print('.eslintrc.cjs adjusted...')

    print("root: " + root)

    # Renames title of HTML index and removes React logo
    index_path = os.path.join(root, 'index.html')
    print(index_path)
    index = open(index_path, 'w')
    index.writelines(get_index_lines(source))
    index.close()
    print('index.html adjusted...')
    
    # Removes Main.css from Main.jsx
    main_path = os.path.join(root, 'src/Main.jsx')
    main = open(main_path, 'w')
    main.writelines(main_lines)
    main.close()
    print('Main.jsx adjusted...')
