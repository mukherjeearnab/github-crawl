from github import Github


def get_repo_files(ACCESS_TOKEN, repository, file_ext=''):
    FILES = []

    # SET GitHub Personal Access Token
    g = Github(ACCESS_TOKEN)

    repositories = g.search_repositories(query='language:python')

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


def get_repo_language(ACCESS_TOKEN, repo_language, file_ext=''):

    REPO_FILES = []

    # SET GitHub Personal Access Token
    g = Github(ACCESS_TOKEN)

    # GET repositories with language
    repositories = g.search_repositories(query=f'language:{repo_language}')

    # ITERATE repositories
    for repo in repositories:
        FILES = get_repo_files(access_token=ACCESS_TOKEN,
                               repository=repo, file_ext=file_ext)
        REPO = {'repository': repo.name, 'files': FILES}
        REPO_FILES.append(REPO)

        return REPO_FILES
