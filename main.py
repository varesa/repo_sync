from githubAPI import Github
from gitlabAPI import Gitlab
from git import Git

import os.path

def main():
    github = Github()
    gitlab = Gitlab()

    repos_gh = github.get_repos('varesa')
    repos_gl = gitlab.get_repos()

    create_missing(repos_gh, repos_gl, gitlab)

    sync(repos_gh, gitlab)


def sync(repos_gh, gitlab):
    git = Git()

    for repo_gh in repos_gh:
        name = repo_gh['name']
        repo_gl = gitlab.get_repo(name)
        if git.repo_exists(name):
            print("repo exists")
        else:
            print("no repo, creating")
            print(git.repo_create(repo_gh, repo_gl))


def create_missing(repos_gh, repos_gl, gitlab):
    for repo_gh in repos_gh:
        found = False
        for repo_gl in repos_gl:
            if repo_gh['name'] == repo_gl['name']:
                found = True

        if not found:
            print("Creating repo " + repo_gh['name'])
            print(gitlab.create_repo(repo_gh['name']))


if __name__ == "__main__":
    main()

