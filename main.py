import crawl

ACCESS_TOKEN = 'access_token'
REPOSITORY = 'repository'
FILE_EXTENTION = 'file_ext'

FILES = crawl.get_files(ACCESS_TOKEN, REPOSITORY, FILE_EXTENTION)

print(FILES)
