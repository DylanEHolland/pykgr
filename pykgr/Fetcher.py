import subprocess

class Fetcher(object):
    def fromTar(self, url):
        subprocess.run(["wget", "-c", url])