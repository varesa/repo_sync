import os
import subprocess

class Git:
    def __init__(self):
        self.PATH_BASE = os.path.join(os.path.expanduser("~"), "repo_sync")
        print(self.PATH_BASE)
        if not os.path.isdir(self.PATH_BASE):
            os.mkdir(self.PATH_BASE)

    def repo_exists(self, name):
        return os.path.isdir(os.path.join(self.PATH_BASE, name))

    def repo_path(self, name):
        return os.path.join(self.PATH_BASE, name)

    def repo_create(self, repo, mirror):
        out = subprocess.check_output(['git', 'clone', repo['ssh_url']], cwd=self.PATH_BASE, stderr=subprocess.STDOUT)
        out += subprocess.check_output(['git', 'remote', 'add', 'gitlab', mirror['ssh_url_to_repo']], cwd=self.repo_path(repo['name']), stderr=subprocess.STDOUT)

        return out

    def repo_sync(self, repo):
        out = subprocess.check_output(['git', 'pull', 'origin', '*:*'], cwd=self.repo_path(repo['name']), stderr=subprocess.STDOUT)
        try:
            out += subprocess.check_output(['git', 'pull', 'gitlab', '*:*'], cwd=self.repo_path(repo['name']), stderr=subprocess.STDOUT)
        except:
            pass # Fails on the first run when the mirror is empty
        out += subprocess.check_output(['git', 'push', 'origin', '*:*'], cwd=self.repo_path(repo['name']), stderr=subprocess.STDOUT)
        out += subprocess.check_output(['git', 'push', 'gitlab', '*:*'], cwd=self.repo_path(repo['name']), stderr=subprocess.STDOUT)

        return out