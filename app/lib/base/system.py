import os


class SystemManager:
    def __init__(self, shell, settings):
        self.shell = shell
        self.settings = settings

    def update_hashcat_version(self):
        hashcat_binary = self.settings.get('hashcat_binary', '')
        if len(hashcat_binary) == 0:
            return False
        elif not os.path.isfile(hashcat_binary):
            return False
        elif not os.access(hashcat_binary, os.X_OK):
            return False

        version = self.shell.execute([hashcat_binary, '--version'])
        self.settings.save('hashcat_version', version)
        return True

    def update_git_hash_version(self):
        git_binary = self.shell.execute(['which', 'git'])
        if len(git_binary) == 0:
            return False

        version = self.shell.execute(['git', 'rev-parse', '--short', 'HEAD'])
        self.settings.save('git_hash_version', version)
        return True
