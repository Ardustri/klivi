import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="klivi",
    version="0.3.0",
    description="klivi, build cross platform desktop app with html",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ardustri/klivi",
    author="Ardustri",
    author_email="contact@klivi.ardustri.org",
    license="MPL-2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=["klivi"],
    include_package_data=True,
    install_requires=["colorama", "pywebview", "xmltodict"],
    entry_points={
        "console_scripts": [
            "klivi=klivi.__main__:main",
        ]
    },
)
