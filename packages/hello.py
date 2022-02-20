class hello(Package):
    source_tarball = "https://ftp.gnu.org/gnu/hello/hello-2.7.tar.xz"

    def compile(self):
        run_cmd("make")

    def pre_compile(self):
        if not exists("build"):
            mkdir("build")
        else:
            run_cmd("rm", "-rf", "build")
            mkdir("build")

        chdir("build")
        run_cmd("../hello-2.7/configure", f"--prefix={self.installation_dir()}")

    def post_compile(self):
        run_cmd("chmod", "+x", "../hello-2.7/build-aux/install-sh") # Fix issue in install :/
        run_cmd("make", "install")

        print(self.installation_dir(), f"{Config.system_directory}/bin")
