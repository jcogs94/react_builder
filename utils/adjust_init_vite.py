import os
from data.vite_config_lines import vite_config_lines
from data.lint_lines import lint_lines
from data.main_lines import main_lines
from data.get_index_lines import get_index_lines
from data.get_app_jsx_lines import get_app_jsx_lines
from data.app_css_lines import app_css_lines


# "Cleans" up default Vite files
def adjust_init_vite(source, base_was_init):
    root = source.replace('/src/components', '')

    print('\nAdjusting vite install...\n')

    # Wipes the init README clean
    readme_path = os.path.join(root, 'README.md')
    readme = open(readme_path, 'w')
    readme.close()
    print('README.md adjusted...')

    # Adds lines to vite.config for later deploy
    config_path = os.path.join(root, 'vite.config.js')
    config = open(config_path, 'w')
    config.writelines(vite_config_lines)
    config.close()
    print('vite.config.js adjusted...')

    # Adds lines to lint
    lint_path = os.path.join(root, '.eslintrc.cjs')
    lint = open(lint_path, 'w')
    lint.writelines(lint_lines)
    lint.close()
    print('.eslintrc.cjs adjusted...')

    # Renames title of HTML index and removes React logo
    index_path = os.path.join(root, 'index.html')
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
    
    # Cleans up the default App.jsx file and inserts base component references
    app_jsx_path = os.path.join(root, 'src/App.jsx')
    app_jsx = open(app_jsx_path, 'w')
    app_jsx.writelines(get_app_jsx_lines(base_was_init))
    app_jsx.close()
    print('App.jsx adjusted...')

    # Cleans up the default App.css file by putting in default styles
    app_css_path = os.path.join(root, 'src/App.css')
    app_css = open(app_css_path, 'w')
    app_css.writelines(app_css_lines)
    app_css.close()
    print('App.css adjusted...')
