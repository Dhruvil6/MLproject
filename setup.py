from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This func will return list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]
        Hypen = '-e .'
        if Hypen in requirements:
            requirements.remove(Hypen)

    return requirements

setup(
    name = 'MLproject',
    version='0.0.1',
    author='Dhruvil',
    author_email='foreverstar1998@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)