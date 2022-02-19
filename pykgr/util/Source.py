from pykgr.Fetcher import Fetcher
from pykgr.util.Helpers import run_cmd
from os.path import basename


def extract_source_from_url(source_url):
    Fetcher().fromTar(source_url)
    file_name = basename(source_url)
    run_cmd("tar", "xvf", file_name)