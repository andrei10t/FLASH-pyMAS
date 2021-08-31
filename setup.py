#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Andrei Toader",
    author_email='andrei.toader32@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="MAS framework for monitoring and deployment",
    entry_points={
        'console_scripts': [
            'flash_pymas=flash_pymas.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='flash_pymas',
    name='flash_pymas',
    packages=find_packages(include=['flash_pymas', 'flash_pymas.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/andrei10t/flash_pymas',
    version='0.1.0',
    zip_safe=False,
)
