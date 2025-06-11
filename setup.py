# from setuptools import find_packages, setup
# setup(
#     name = 'Machine learning project',
#     version = '0.0.1',
#     author = 'Konneh Idrissa',
#     author_email = 'konnehidrissa@gmail.com',
#     packages = find_packages(),
#     install_requires = get_requirements(requirements.txt)
#     #['pandas','numpy','seaborn','matplotlib','scikit-learn']
# )
# from setuptools import find_packages, setup
# from typing import List


# HYPEN_E_DOT = '-e .'
# def get_requirements(file_path: str) -> List[str]:
#     '''
#     This function reads the requirements.txt file and returns a list of packages.
#     '''
#     with open(file_path) as file_obj:
#         requirements = file_obj.readlines()
#         requirements = [req.strip() for req in requirements if req.strip()]

#         if HYPEN_E_DOT in requirements:
#             requirements.remove(HYPEN_E_DOT)
#     return requirements

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads the requirements.txt file and returns a list of packages,
    excluding the editable install line ('-e .') if present.
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='Machine learning project',
    version='0.0.1',
    author='Konneh Idrissa',
    author_email='konnehidrissa@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)