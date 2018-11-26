import os
from setuptools import find_packages, setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='yardsale',
    version='1.1.0',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    license='MIT',
    install_requires=[
        'django',
        'requests'
    ],
    author_email='pkucmus@gmail.com',
    tests_require=['parameterized'],
)
