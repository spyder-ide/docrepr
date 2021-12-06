from setuptools import setup, find_packages
import os

name = 'docrepr'
here = os.path.abspath(os.path.dirname(__file__))

version_ns = {}
with open(os.path.join(here, name, '_version.py')) as f:
    exec(f.read(), {}, version_ns)

setup(
    name=name,
    version=version_ns['__version__'],
    description='docrepr renders Python docstrings in HTML',
    long_description='docrepr renders Python docstrings in HTML. It is based on the sphinxify module developed by Tim Dumol for the Sage Notebook and the utils.inspector developed for ther Spyder IDE.',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['docutils', 'jinja2', 'sphinx<4'],
    url='https://github.com/spyder-ide/docrepr',
    author='Tim Dumol / The Spyder Development Team',
    maintainer='The Spyder Development Team',
    license='BSD',
)
