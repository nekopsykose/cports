pkgname = "krdp"
pkgver = "6.1.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "freerdp",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "freerdp-devel",
    "kcmutils-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kpipewire-devel",
    "kstatusnotifieritem-devel",
    "libxkbcommon-devel",
    "plasma-wayland-protocols",
    "qt6-qtdeclarative-devel",
    "qt6-qtwayland-devel",
    "qtkeychain-devel",
]
pkgdesc = "KDE remote desktop KCM"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://invent.kde.org/plasma/krdp"
source = f"$(KDE_SITE)/plasma/{pkgver}/krdp-{pkgver}.tar.xz"
sha256 = "3127ebb48d130ff1aeb83e0a6598fb22fd0b1264bbe81a9d6c3dd2c38a801890"
# stop_token/jthread
tool_flags = {"CXXFLAGS": ["-fexperimental-library"]}


def post_install(self):
    # TODO: graphical dinit user service
    self.rm(self.destdir / "usr/lib/systemd/user", recursive=True)


@subpackage("krdp-devel")
def _devel(self):
    self.depends += [
        "extra-cmake-modules",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()
