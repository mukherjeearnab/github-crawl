# import crawl

# ACCESS_TOKEN = 'access_token'
# REPOSITORY = 'repository'
# FILE_EXTENTION = '.ext'

# FILES = crawl.get_repo_language(ACCESS_TOKEN, REPOSITORY, FILE_EXTENTION)

# print(FILES)

import clone
import os
from shutil import copyfile

FILE_PATH = './PAYLOAD.txt'

with open(FILE_PATH) as f:
    repositories = f.read().splitlines()

for repository in repositories:
    clone.clone_repo(repository)

# SET extension for target files
TARGET_EXT = '.go'

for path, subdirs, files in os.walk('./clone'):
    for name in files:
        if name.endswith(TARGET_EXT):
            src = os.path.join(path, name)
            dst_name = src.replace('./clone', '')
            dst = os.path.join(
                './targets', dst_name.replace('/', '_'))
            print(dst)
            print('FOUND', src)
            copyfile(src, dst)
            print('COPIED', dst)
