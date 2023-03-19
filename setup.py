from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='nombre_del_proyecto',
    version='0.1',
    packages=find_packages(),
    install_requires=requirements,
)
