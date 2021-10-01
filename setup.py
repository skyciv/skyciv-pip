import setuptools

with open("./README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="skyciv",
    version="2.0.4",
    description="A simplified way to use the SkyCiv API with Python.",
    py_modules=["skyciv"],
    package_dir={"": "src"},
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="skyciv structural analysis design API AISC Eurocode CSA steel concrete BIM",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    extras_require={
        "dev": [
            "pytest>=3.7"
        ]
    },
    url="https://github.com/skyciv/skyciv-pip",
    author="Steve Richardson",
    author_email="steve.richardson@skyciv.com",
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=['typing-extensions']
)
