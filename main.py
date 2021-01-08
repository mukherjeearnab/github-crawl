import crawl

ACCESS_TOKEN = 'access_token'
REPOSITORY = 'repository'
FILE_EXTENTION = '.ext'

FILES = crawl.get_repo_language(ACCESS_TOKEN, REPOSITORY, FILE_EXTENTION)

print(FILES)
