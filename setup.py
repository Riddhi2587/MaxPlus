from setuptools import find_packages, setup

setup(
    name='maxplus',
    packages=find_packages(include=['maxplus']),
    version='0.1.0',
    description='',
    author='',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)