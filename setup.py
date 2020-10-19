from setuptools import setup

long_description = ''
with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='skyciv',
    version='0.0.1',
    description='A simplified way to use the SkyCiv API.',
    py_modules=["skyciv"],
    package_dir={'': 'src'},
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    extras_require={
        "dev": [
            "pytest>=3.7",
        ]
    },
    url="",
    author="Steve Richardson",
    author_email="steve.richardson@skyciv.com",
)