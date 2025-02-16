from setuptools import find_packages,setup

setup(
name='mlproject',
version='0.0.1',
author='Shubham Jha',
email='shubhamjha014@gmail.com',
packages=find_packages(), ## It will find everywhere where "__init___.py" is and consider it's folder as a package.
install_requires=['pandas','numpy','seaborn']

)