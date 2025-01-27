#this is just the setup file I'm going to use.
from setuptools import find_packages,setup
from typing import List



def get_requirements(file_path:str)->List[str]:
    '''
    this is the function to return all the packages we want in requirements.txt file, as a list
    '''
    requirements = []
    with open(file_path) as file_obj:
        lines = file_obj.readlines()
        requirements = [line.strip() for line in lines if line.strip() and line.strip() != '-e .']

        return requirements





setup(
name= 'ml_project',
version = '0.1',
author = 'TheJ Nihas',
author_email='tejnihashrevu361@gmail.com',
packages= find_packages(),
install_requires = get_requirements('requirements.txt')







)