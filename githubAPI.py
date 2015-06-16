import json
from requests import get


class Github():
    URL_BASE = "https://api.github.com"

    def __init__(self):
        pass

    def get_repos(self, user):
        repos = []
        page = 1
        while True:
            response = get(self.URL_BASE + "/users/" + user + "/repos?page=" + str(page))
            repos += json.loads(response.text)
            if 'last' not in response.headers['link']:
                break
            page += 1
        return repos