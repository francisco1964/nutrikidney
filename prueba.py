import sys
import os

def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

if len(sys.argv) > 1:
    print(sys.argv[1:])


for file in get_files('files/'):
    print(file)