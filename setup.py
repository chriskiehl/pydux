from os.path import abspath, dirname, join
from setuptools import setup, find_packages

INIT_FILE = join(dirname(abspath(__file__)), 'pydux', '__init__.py')

def get_version():
    with open(INIT_FILE) as fd:
        for line in fd:
            if line.startswith('__version__'):
                version = line.split()[-1].strip('\'')
                return version
        raise AttributeError('Package does not have a __version__')

setup(
    name='pydux',
    description="Python + Redux = Pydux",
    long_description=open('README.md').read(),
    url="http://github.com/benjamin9999/pydux/",
    version=get_version(),
    author='Benjamin Yates',
    author_email='benjamin@rqdq.com',
    packages=['pydux'],
    install_requires=[],
    license='MIT',
)

