from setuptools import find_packages,setup
from typing import List

REQUIREMENTS_FILE = 'requirements.txt'
HYPHEN_E_DOT = '-e .'

def get_requirements(req_file) -> List[str]:
    with open(req_file) as file_obj:
        read_requirements = file_obj.readlines()
        requirements_list = [requirement.replace('\n',"") for requirement in read_requirements]

        if HYPHEN_E_DOT in requirements_list:
            requirements_list.remove(HYPHEN_E_DOT)
    return requirements_list

setup(
    name='sensor',
    version='0.0.1',
    author='Deepjyoti Bhattacharjee',
    author_email='deepjyotibhattacharjee217@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements(REQUIREMENTS_FILE)
)
