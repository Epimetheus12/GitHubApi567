'''
Fangji Liang HW04a
'''
from urllib import request, error
import re
import json


class UrlOpenError(Exception):
    '''url exception'''
    pass


def get_repo(id):
    '''
    get repo name of github_id, then get each number of commits of repos
    return repos and commits
    '''
    url_repo = f"https://api.github.com/users/{id}/repos"

    try:
        repo = request.urlopen(url_repo)
    except error.HTTPError as e:
        raise UrlOpenError(f"{url_repo} -- Can't open this page. Error：" + str(e.code))
    except error.URLError as e:
        raise UrlOpenError("Network connection timed out or failed")
    
    regex = re.compile(r"(?<=\"name\":\").+?(?=\")", flags=re.IGNORECASE)
    temp_repo = re.findall(regex, str(repo.read()))
    result = []

    for repo in temp_repo:
        url_com = f"https://api.github.com/repos/{id}/{repo}/commits"
        try:
            com = request.urlopen(url_com).read()
        except error.HTTPError as e:
            raise UrlOpenError(f"{url_com} -- Can't open this page. Error：" + str(e.code))
        except error.URLError as e:
            raise UrlOpenError("Network connection timed out or failed")
        
        result.append((f"Repo: {repo} Number of commits: {len(json.loads(com))}"))   
    return result
            
            
def main():
    for i in get_repo('Epimetheus12'):
        print(i)

if __name__ == "__main__":
    main()