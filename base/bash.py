import pykgr
import os

class bash(pykgr.Package):
    file_url = "http://ftp.gnu.org/gnu/bash/bash-5.0.tar.gz"
    file_name = "bash-5.0.tar.gz"
    name = "bash"
    version = "5.0"

    def fetch(self):
        self.shell.cd(pykgr.config.source_tarballs_directory)
        if os.path.exists(self.code_directory):
            print("Already exists")
            return

        self.shell.command(
            "wget", 
            "-c",
            self.file_url
        ).run(
            display_output = True
        )

        self.shell.tar(
            "xvf",
            self.file_name,
            "-C",
            pykgr.config.source_directory,
            display_output = True
        )

    def install(self):
        self.shell.cd(self.build_directory)
        self.shell.make(
            "-j%s" % pykgr.config.make_opts,
            "install",
            display_output = True
        )

    def make(self):
        self.shell.cd(self.build_directory)
        self.shell.make("-j%s" % pykgr.config.make_opts, display_output = True)
        
    def prepare(self):
        self.shell.cd(self.code_directory)
        if not os.path.exists(self.build_directory):
            os.mkdir(self.build_directory)
        self.shell.cd(self.build_directory)

        self.shell.command(
            "%s/configure" % self.code_directory,
            "--prefix=%s" % pykgr.config.builder_directory
        ).run(display_output = True)
