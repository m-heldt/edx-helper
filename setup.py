# -*- coding: utf-8 -*-
#
# you can install this to a local test virtualenv like so:
#   virtualenv venv
#   ./venv/bin/pip install --editable .
#   ./venv/bin/pip install --editable .[dev]  # with dev requirements, too

from __future__ import print_function

from setuptools import setup

from edx_helper import __version__


def read_file(filename, alt=None):
    """
    Read the contents of filename or give an alternative result instead.
    """
    try:
        with open(filename, encoding='utf-8') as f:
            return f.read()
    except IOError:
        return [] if alt is None else alt


long_description = read_file(
    'README.md',
    'Cannot find README.md'
)
requirements = read_file('requirements.txt')
dev_requirements = read_file('requirements-dev.txt')

trove_classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: End Users/Desktop',
    'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Education',
]

setup(
    name='edx-helper',
    version=__version__,
    maintainer='Ye Zheng',
    maintainer_email='csyezheng@gmail.com',

    license='LGPL',
    url='https://github.com/csyezheng/edx-helper',

    install_requires=requirements,
    extras_require={
        'dev': dev_requirements,
    },

    description='Simple tool to download video and lecture materials from edx.org.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['edx-helper', 'edx-dl', 'edX', 'download', 'education', 'MOOCs', 'video'],
    classifiers=trove_classifiers,

    packages=["edx_helper"],
    entry_points=dict(
        console_scripts=[
            'edx-helper=edx_helper.edx_dl:main'
        ]
    ),

    platforms=['any'],
)
