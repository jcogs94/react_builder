import os
from utils.get_source import get_source
from utils.change_to_components_dir import change_to_components_dir
from utils.new_project import new_project
from utils.build_components import build_components


os.system('cls' if os.name == 'nt' else 'clear')
print('Welcome to the React Manager App!\n')

source = get_source()
source = change_to_components_dir(source)

new_project(source)
build_components(source)

# /home/jcogs/code/sandbox/python_scripts_testing
