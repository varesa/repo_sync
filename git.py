import os
import subprocess
import traceback

class Git:
    def __init__(self):
        self.PATH_BASE = os.path.join(os.path.expanduser("~"), "repo_sync")
        if not os.path.isdir(self.PATH_BASE):
            os.mkdir(self.PATH_BASE)

    def repo_exists(self, name):
        return os.path.isdir(os.path.join(self.PATH_BASE, name))

    def repo_path(self, name):
        return os.path.join(self.PATH_BASE, name)

    def repo_create(self, repo, mirror):
        try:
            out = subprocess.check_output(['git', 'clone', repo['ssh_url']], cwd=self.PATH_BASE, stderr=subprocess.STDOUT)
            out += subprocess.check_output(['git', 'remote', 'add', 'gitlab', mirror['ssh_url_to_repo']], cwd=self.repo_path(repo['name']), stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError:
            traceback.print_exc()

        return out.decode()

    def repo_sync(self, repo):
        try:
            out = subprocess.check_output(['git', 'pull', '--all'], cwd=self.repo_path(repo['name']), stderr=subprocess.STDOUT)
            out += subprocess.check_output(['git', 'push', 'origin', '*:*'], cwd=self.repo_path(repo['name']), stderr=subprocess.STDOUT)
            out += subprocess.check_output(['git', 'push', 'gitlab', '*:*'], cwd=self.repo_path(repo['name']), stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError:
            traceback.print_exc(),

        return out.decode()