import os

import pkg_resources
from setuptools import setup, find_packages


setup(
    name="kcg-ipfs",
    py_modules=[],
    version="1.0",
    description="",
    author="kcg",
    packages=find_packages(),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    entry_points={
        "console_scripts": [
        ]
    }
)
