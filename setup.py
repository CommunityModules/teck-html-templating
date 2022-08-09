#!/usr/bin/env python
import setuptools

VERSION = "0.1.2"


def readme():
    with open("README.md") as file:
        return file.read()


setuptools.setup(
    name="teck-html-templating",
    version=VERSION,
    python_requires=">=3.8",
    author="Trent Millar",
    description="Templating engine to transform map data to HTML",
    long_description=readme(),
    url="https://github.com/CommunityModules/teck-html-templating",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=[
        "jinja2==3.1.2"
    ],
    include_package_data=True
)
