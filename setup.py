from setuptools import setup, find_packages

setup(
    name='xray-enhancement-algorithm',  # Package name
    version='0.1.0',  # Package version
    author='veeravaishnavi2007-wq',  # Author name
    description='A Python package for X-ray enhancement algorithms.',  # Short description
    packages=find_packages(),  # Automatically find packages in the source code
    install_requires=[  # List of dependencies
        'numpy',
        'scipy',
        'opencv-python',
        'matplotlib',
        # add any other dependencies here
    ],
)