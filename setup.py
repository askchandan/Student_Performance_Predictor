from setuptools import find_packages,setup # It will find all the packages in the machine learning application
from typing import List


HYPHEN_E_DOT = "-e ."


def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='Student_Performance_Predictor',
    version='0.0.1',
    author='Chandan Malakar',
    author_email='chandanmalakar6209@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)

# using setup.py I can install my machine learning application as a package

