from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """This function returns the list of requirements from the file."""
    requirements = []
    with open(file_path) as fileobj:
        requirements = fileobj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='Project-Practice',
    author_email='abhishek.7979883@gmail.com',
    version='0.0.1',
    author='Abhishek',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
