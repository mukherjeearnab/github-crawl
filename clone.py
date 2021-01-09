import subprocess


def clone_repo(repository):
    try:
        url = f'https://github.com/{str(repository)}'
        result = subprocess.run(
            ['git', 'clone', url, f'./clone/{str(repository).split("/")[-1]}'], stdout=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))

    except Exception as e:
        print('ERROR!', e)
