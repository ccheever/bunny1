#!/usr/bin/env python
from setuptools import setup

setup(
    name="bunny1",
    version="1.1",
    description="bunny1 is a tool that lets you write smart bookmarks in " +
        "python and then share them across all your browsers and with a " +
        "group of people or the whole world.",
    author="facebook",
    author_email="bunny1-feedback@lists.facebook.com",
    url="http://www.bunny1.org/",
    packages=["bunny1"],
    package_dir={"bunny1": "src"},
    package_data={"bunny1": ["README", "LICENSE", "*.gif", "*.ico"]},
    scripts=["src/b1_example.py", "src/b1_barebones.py"],
    install_requires=["cherrypy>=3.1.0"],
)
