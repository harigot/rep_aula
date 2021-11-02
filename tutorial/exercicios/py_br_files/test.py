import os
from pathlib import Path


'''
path = '/home/harigot/Documents/repositorios/rep_aula/tutorial/exercicios/py_br_files/files/ip_database.txt'
  
# Path of Start directory
start = '/home/harigot/Documents/repositorios/rep_aula'

# Compute the relative file path
# to the given path from the 
# the given start directory.
relative_path = os.path.relpath(path, start)

print(relative_path)
'''
'''
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
'''
mod_path = Path(__file__).parent
relative_path_1 = 'tutorial/exercicios/py_br_files/files/ip_database.txt'

src_path_1 = (mod_path / relative_path_1).resolve()
print(src_path_1)