#!/usr/bin/env python
# -*- coding: utf-8; fill-column: 100 -*-
#
# Copyright (C) 2021 CFEL Controlled Molecule Imaging group

from setuptools import setup, find_packages
copyright = 'Copyright (C) 2021 Yahya Saleh <yahya.saleh@cfel.de> and Jochen Küpper <jochen.kuepper@cfel.de>'
name = "ALPES"
version = "1.0"
release = version
long_description = """ALPES: Stochastic active learning of PES

This is the installation and general build file of the CMI Active Learning of PES code. The code
demonstrates how to use the active learning algorithms developed in arXiv:2104.00708 [physics] to
construct potential energy surfaces of pyrrole water molecules.

Author:             Yahya Saleh, Vishnu Sanjay, and the CFEL Controlled Molecule Imaging group
                    https://www.controlled-molecule-imaging.org
Current maintainer: Yahya Saleh <yahya.saleh@cfel.de>
"""

classifiers = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Operating System :: POSIX :: Linux',
    'Operating System :: Unix',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Physics',
    'Topic :: Scientific/Engineering :: Chemistry',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
]

with open('requirements.txt') as of:
    install_requires = of.read().splitlines()

setup(name=name,
      python_requires     = '~=3.7',
      author              = "Yahya Saleh, Vishnu Sanjay, and the CFEL-CMI group",
      author_email        = "yahya.saleh@cfel.de",
      maintainer          = "Yahya Saleh and the CFEL-CMI group",
      maintainer_email    = "yahya.saleh@cfel.de",
      url                 = "https://github.com/CFEL-CMI/Active-Learning-of-PES",
      description         = "CMI Active Learning of PES",
      version             = version,
      long_description    = long_description,
      license             = "GPL",
      packages            = ['ALPES'],
      install_requires    = install_requires, 
      command_options     = {
          'build_sphinx': {
              'project': ('setup.py', name),
              'version': ('setup.py', version),
              'release': ('setup.py', release),
              'source_dir': ('setup.py', 'docs/source'),
              'copyright': ('setup.py', copyright)}
      },
      classifiers         = classifiers,
      )
