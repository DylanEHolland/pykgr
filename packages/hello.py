class hello(Package):
    source_tarball = "https://ftp.gnu.org/gnu/hello/hello-2.7.tar.xz"

    def pre_compile(self):
        if not exists("build"):
            mkdir("build")
        else:
            run_cmd("rm", "-rf", "build")
            mkdir("build")

        chdir("build")
        run_cmd("ls", "../")
        run_cmd("../hello-2.7/configure")

    def compile(self):
        run_cmd("make")

    def post_compile(self):
        run_cmd("make", "install")
