from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

    setup(
        name="MLOPS_Project_6",
        version="0.1",
        author="Prince",
        packages=find_packages(),
        install_requires=requirements,
    )