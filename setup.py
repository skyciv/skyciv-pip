from setuptools import setup

long_description = ''
with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='skyciv',
    version='1.0.2',
    description='A simplified way to use the SkyCiv API with Python.',
    py_modules=["skyciv"],
    package_dir={'': 'src'},
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='skyciv structural analysis design API AISC Eurocode CSA steel concrete BIM',
    classifiers=[
        'License :: OSI Approved :: MIT License',
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
    url="https://github.com/skyciv/skyciv-pip",
    author="Steve Richardson",
    author_email="steve.richardson@skyciv.com",
)
