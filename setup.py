# pylint: skip-file

import setuptools
import sys
import pathlib

from importlib.machinery import SourceFileLoader
from os import path

if sys.version_info < (3, 0):
    raise RuntimeError("notify requires Python 3.0+")

HERE = pathlib.Path(__file__).parent
IS_GIT_REPO = (HERE / '.git').exists()

module = SourceFileLoader(
    fullname="version", path=path.join("notify", "version.py"),
).load_module()

libraries = []

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("CHANGELOG.md", "r", encoding="utf-8") as fp:
    changes = fp.read()

setuptools.setup(
    name="notify",
    version=module.__version__,
    packages=["notify"],
    author=module.__author__,
    author_email=module.team_email,
    description=module.package_info,
    long_description=long_description + '\n\n' + changes,
    long_description_content_type="text/markdown",
    url="",
    project_urls={
        'Gitlab: issues': '',
        'Gitlab: repo': '',
        'Read the Docs': ''
    },
    classifiers=[
        "Environment :: Console",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows'
    ],
    python_requires=">=3.0",
    install_requires=open('requirements.txt').read().split('\n')
)
