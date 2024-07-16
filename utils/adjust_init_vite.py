import os
from data.lint_lines import lint_lines
from data.main_lines import main_lines

def adjust_init_vite(source):
    root = source.replace('/src/components', '')

    print('\nAdjusting vite install...')

    lint_path = os.path.join(root, '.eslintrc.cjs')
    lint = open(lint_path, 'w')
    lint.writelines(lint_lines)
    lint.close()
    print('.eslintrc.cjs adjusted...')

    main_path = os.path.join(root, '/src/main.jsx')
    main = open(main_path, 'w')
    main.writelines(main_lines)
    main.close()
    print('main.jsx adjusted...')
    
    main_path = os.path.join(root, '/src/main.jsx')
    main = open(main_path, 'w')
    main.writelines(main_lines)
    main.close()
    print('main.jsx adjusted...')
