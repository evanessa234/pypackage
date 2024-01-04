from setuptools import setup, find_packages

setup(
    name='pypackage',  # Package name
    version='0.1.0',    # Version
    author='Heena Singh',
    author_email='heenareenasingh234@gmail.com',
    description='Testing out python library creation',
    packages=find_packages(),  # Automatically finds packages/modules
    install_requires=[        # List any required dependencies
        'numpy',
        'pandas',
        # ...
    ],
)