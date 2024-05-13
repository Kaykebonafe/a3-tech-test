from setuptools import setup, find_packages
from a3_tech_test.__init__ import __version__

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='A3_Tech_Test',
    version=__version__,
    author='Kayke B. Kakazu',
    author_email='kayke.bonafe98@gmail.com',
    packages=find_packages(),
    install_requires=requirements,
)
