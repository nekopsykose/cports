pkgname = "libuv"
pkgver = "1.47.0"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
pkgdesc = "Multi-platform support library with focus on asynchronous I/O"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://libuv.org"
source = (
    f"https://dist.libuv.org/dist/v{pkgver}/{pkgname}-v{pkgver}-dist.tar.gz"
)
sha256 = "e585d22b4d158e1e6a4e51a91f4392250e3bd1f7828c0d270aad647b297da334"
# FIXME cfi
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libuv-devel")
def _devel(self):
    return self.default_devel()
