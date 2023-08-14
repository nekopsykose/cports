pkgname = "xdg-desktop-portal"
pkgver = "1.17.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "bubblewrap", "glib-devel"]
makedepends = [
    "flatpak-devel",
    "json-glib-devel",
    "fuse-devel",
    "gdk-pixbuf-devel",
    "pipewire-devel",
    "libportal-devel",
    "geoclue-devel",
]
checkdepends = ["bash", "dbus"]
pkgdesc = "Desktop integration portal"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1-or-later"
url = "https://github.com/flatpak/xdg-desktop-portal"
source = f"https://github.com/flatpak/xdg-desktop-portal/releases/download/{pkgver}/xdg-desktop-portal-{pkgver}.tar.xz"
sha256 = "cafa7c4289decf203d21829abbbefc3e968c9975664685e151db2c701b532a8b"


def post_install(self):
    self.rm(self.destdir / "usr/lib/systemd", recursive=True)


@subpackage("xdg-desktop-portal-devel")
def _devel(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    return self.default_devel()
