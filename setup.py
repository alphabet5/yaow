import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("yaow/VERSION", "r") as f:
    version = f.read()

setuptools.setup(
    name="yaow",
    version=version,
    author="alphabet5",
    description="Yet another openconnect wrapper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alphabet5/yaow",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    entry_points={"console_scripts": ["yaow=yaow.cli:main"]},
    include_package_data=True,
    package_data={
        "yaow": ["*"],
    },
    install_requires=[
        "validators",
        "yamlarg",
        "keyring",
        "pyotp",
        "O365",
        "rich",
    ],
)
