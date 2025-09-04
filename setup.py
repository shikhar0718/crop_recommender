from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:

    reqirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        reqirements=[req.replace("\n"," ")for req in reqirements]

        if HYPHEN_E_DOT in reqirements:
            reqirements.remove(HYPHEN_E_DOT)

    return reqirements

setup(
    name='crop recommender',
    version='0.0.1',
    author='shikhar',
    author_email='shikhar0718@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)