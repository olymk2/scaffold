import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "scaffold",
    version = "0.0.5",
    author = "Oliver Marks",
    author_email = "olymk2@gmail.com",
    description = ("Web templating library"),
    license = "GPL",
    keywords = "templating web",
    url = "https://code.launchpad.net/~oly/scaffold/trunk",
    packages=find_packages(),
    
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)

