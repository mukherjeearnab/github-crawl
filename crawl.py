from github import Github


def get_repo_files(access_token, repository, file_ext=''):
    FILES = []

    # SET GitHub Personal Access Token
    g = Github(access_token)

    # SET Repository e.g. mukherjeearnab/policing-network
    repo = g.get_repo(repository)

    # GET  all repository contents
    contents = repo.get_contents("")
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            if str(file_content.name).endswith(file_ext):
                file_dict = {'name': file_content.name,
                             'download_url': file_content.download_url}
                FILES.append(file_dict)

    return FILES


def get_repo_language(access_token, repo_language, file_ext='', limit=5):

    REPO_FILES = []

    # SET GitHub Personal Access Token
    g = Github(access_token)

    # GET repositories with language
    repositories = g.search_repositories(query=f'language:{repo_language}')
    # SET index
    index = 0

    # ITERATE repositories
    for repo in repositories:
        # CHECK limit
        if index >= limit:
            break

        print('CRAWL', repo.full_name)
        try:
            FILES = get_repo_files(access_token=access_token,
                                   repository=repo.full_name, file_ext=file_ext)
            REPO = {'repository': repo.full_name, 'files': FILES}
            REPO_FILES.append(REPO)
            print('DONE', REPO['repository'])

            # Increment index
            index += 1
        except Exception as e:
            print('Error!\n', e)

    return REPO_FILES
