from setuptools import setup, find_packages
import autoprefixer

setup(
    name='autoprefixer',
    version=autoprefixer.__version__,
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'optional-django>=0.3.0'
    ],
    author='Mark Finger',
    author_email='markfinger@gmail.com',
    url='https://github.com/markfinger/python-autoprefixer',
)