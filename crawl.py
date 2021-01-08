from github import Github


def get_files(ACCESS_TOKEN, repository, file_ext):
    FILES = []

    # SET GitHub Personal Access Token
    g = Github(ACCESS_TOKEN)

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
