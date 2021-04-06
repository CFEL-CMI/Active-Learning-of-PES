#!/usr/bin/env python
# -*- coding: utf-8; fill-column: 120 -*-
#
# Copyright (C) 2021 CFEL Controlled Molecule Imaging group

from setuptools import setup, find_packages

copyright = 'Copyright (C) 2021 Jochen Küpper <jochen.kuepper@cfel.de>'
name = "Active Learning of PES"
version = "1.0"
release = version
long_description = """Active Learning of PES

This is the installation and general build file of the CMI Active Learning of PES code,
which is part of and documented in ...

Author:             Yahya Saleh, Vishnu Sanjay, and the CFEL Controlled Molecule Imaging group <jochen.kuepper@cfel.de>
Current maintainer: Yahya Saleh <yahya.saleh@cfel.de>
"""

setup(name=name,
      python_requires     = '>=3.8',
      author              = "Yahya Saleh, Vishnu Sanjay, and the CFEL-CMI group",
      author_email        = "jochen.kuepper@cfel.de",
      maintainer          = "Yahya Saleh and the CFEL-CMI group",
      maintainer_email    = "yahya.saleh@cfel.de",
      url                 = "https://github.com/CFEL-CMI/CMI-Python-project-template",
      description         = "CMI Active Learning of PES",
      version             = version,
      long_description    = long_description,
      license             = "GPL",
      package_dir         = package_dir,
      packages            = find_packages(where='scripts'),
      #scripts             = ['scripts/alpes'],
      command_options     = {
          'build_sphinx': {
              'project': ('setup.py', name),
              'version': ('setup.py', version),
              'release': ('setup.py', release),
              'source_dir': ('setup.py', 'doc'),
              'copyright': ('setup.py', copyright)}
      },
      install_requires     = ['tensorflow>=2.2']
      )
