#!/usr/bin/env python
# -*- coding: utf-8; fill-column: 120 -*-
#
# Copyright (C) 2020 Jochen Küpper <jochen.kuepper@cfel.de>

from setuptools import setup

copyright = 'Copyright (C) 2020 Jochen Küpper <jochen.kuepper@cfel.de>'
name = "Active Learning of PES"
version = "1.0"
release = version
long_description = """Active Learning of PES

This is the installation and general build file of the CMI Active Learning of PES code,
which is part of and documented in ...

Original author:    Jochen Küpper <jochen.kuepper@cfel.de>
Current maintainer: Jochen Küpper <jochen.kuepper@cfel.de>
"""


setup(name=name,
      python_requires     = '>=3.8',
      author              = "Jochen Küpper and the CFEL-CMI group",
      author_email        = "jochen.kuepper@cfel.de",
      maintainer          = "Jochen Küpper and the CFEL-CMI group",
      maintainer_email    = "jochen.kuepper@cfel.de",
      url                 = "https://github.com/CFEL-CMI/CMI-Python-project-template",
      description         = "CMI Active Learning of PES",
      version             = version,
      long_description    = long_description,
      license             = "GPL",
      packages            = ['alpes'],
      scripts             = ['scripts/alpes'],
      command_options={
          'build_sphinx': {
              'project': ('setup.py', name),
              'version': ('setup.py', version),
              'release': ('setup.py', release),
              'source_dir': ('setup.py', 'doc'),
              'copyright': ('setup.py', copyright)}
      },
      )
