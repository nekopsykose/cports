pkgname = "knot-resolver"
pkgver = "6.0.8"
pkgrel = 0
build_style = "meson"
configure_args = [
    # technically, this is deprecated in v6, since they ported to a new
    # python-based manager + kresctl + yaml config, and this is the older
    # lua config
    # but all the new stuff is really systemd dependent and this will stick
    # around for a long time, just with more breaking changes
    "-Dinstall_kresd_conf=enabled",
    "-Dkeyfile_default=/etc/dns/root.key",
    "-Dmanaged_ta=disabled",  # use distro one from above
    "-Dgroup=_kresd",
    "-Duser=_kresd",
    "-Dcapng=enabled",
    "-Ddnstap=enabled",
    "-Dmalloc=disabled",
    "-Dunit_tests=enabled",
    "-Dutils=enabled",
]
hostmakedepends = [
    "bash",
    "meson",
    "pkgconf",
]
makedepends = [
    "cmocka-devel",
    "fstrm-devel",
    "gnutls-devel",
    "knot-devel",
    "libcap-ng-devel",
    "libedit-devel",
    "libuv-devel",
    "lmdb-devel",
    "luajit-devel",
    "nghttp2-devel",
    "protobuf-c-devel",
]
depends = [
    "dnssec-anchors",
    "libcap-progs",
]
pkgdesc = "Caching DNS resolver"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://www.knot-resolver.cz"
source = (
    f"https://secure.nic.cz/files/knot-resolver/knot-resolver-{pkgver}.tar.xz"
)
sha256 = "ac12f000ab599fd2223e418611e77746da717c6ba27654661fa36c847185a266"


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "kresd")
    self.install_service(self.files_path / "kres-cache-gc")


@subpackage("knot-resolver-libs")
def _(self):
    return self.default_libs()


@subpackage("knot-resolver-devel")
def _(self):
    return self.default_devel()
