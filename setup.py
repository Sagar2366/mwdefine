from setuptools import setup, find_packages

setup(
    name="mwdefine",
    version="0.1.0",
    description="Merriam-Webster Dictionary CLI",
    author="Your Name",
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "mwdefine = mwdefine.cli:main"
        ]
    },
)
