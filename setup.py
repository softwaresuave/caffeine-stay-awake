#!/usr/bin/env python
import os
from os import walk

from setuptools import find_packages
from setuptools import setup


def get_data_files():
    data_files = []

    for path, _dirs, files in walk("share"):
        target_path = os.path.join("/usr", path)

        if files:
            data_files.append((target_path, [os.path.join(path, f) for f in files]))

    # Install all icons for the package into /usr/share as well.
    # This is because the .desktop file actually uses them too.
    for path, _dirs, files in walk("caffeine/assets/icons"):
        target_path = os.path.join("/usr/share", path[16:])

        if files:
            data_files.append((target_path, [os.path.join(path, f) for f in files]))

    data_files.append(("/etc/xdg/autostart", ["share/applications/caffeine.desktop"]))

    return data_files


if __name__ == "__main__":
    setup(
        name="caffeine-ng",
        use_scm_version={
            "version_scheme": "post-release",
            "write_to": "caffeine/version.py",
        },
        description=("Tray bar app to temporarily inhibit screensaver and sleep mode."),
        long_description=open("README.rst").read(),
        author="The Caffeine Developers",
        author_email="hugo@barrera.io",
        maintainer="Hugo Osvaldo Barrera",
        maintainer_email="hugo@barrera.io",
        url="https://github.com/caffeine-ng/caffeine-ng",
        packages=find_packages(),
        include_package_data=True,
        data_files=get_data_files(),
        install_requires=[
            "click>=7.1,<8.0",
            "ewmh>=0.1.4",
            "pyxdg>=0.25",
            "setproctitle>=1.1.10",
            "wheel>=0.29.0",
            "pulsectl",
            "pygobject>=3.1.1,<4.0",
        ],
        # `console_scripts` is the same as `gui_scripts`.
        entry_points={"gui_scripts": ["caffeine = caffeine.cli:cli"]},
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: X11 Applications",
            "Environment :: X11 Applications :: GTK",
            "Intended Audience :: End Users/Desktop",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: POSIX",
            "Operating System :: POSIX :: BSD",
            "Operating System :: POSIX :: Linux",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
        ],
        setup_requires=["setuptools_scm"],
    )
