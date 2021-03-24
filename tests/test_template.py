#!/usr/bin/env python
# -*- coding: utf-8; fill-column: 100; truncate-lines: t -*-
#
# This file is part of the CMI Python project template
# Copyright (C) 2008,2020 Jochen Küpper <jochen.kuepper@cfel.de>
#
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU
# General Public License as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# If you use this programm for scientific work, you must correctly reference it; see LICENSE file
# for details.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program. If not, see
# <http://www.gnu.org/licenses/>.
"""Unit-tests of template

Copyright (C) 2020 Jochen Küpper <jochen.kuepper@cfel.de>"""

__author__ = "Jochen Küpper <jochen.kuepper@cfel.de>"

# using pytest we can write very simple tests
def test_template():
    assert(2.*5.-10. == 0.)



# alternativly, we can also use a standard unittest.TestCase setup, which is automatically picked up
# by pytest
import unittest

class TemplateTest(unittest.TestCase):
    """Test the template tests;-)"""

    @classmethod
    def setUpClass(self):
        """Run before the first test"""
        self.variable = 0.

    @classmethod
    def tearDownClass(self):
        """Run after the last test"""
        pass

    def setUp(self):
        """Run before every single test method"""
        pass

    def tearDown(self):
        """Run after every single test method"""
        pass

    def test_template(self):
        """Test the value of variable against some calulated value"""
        self.assertAlmostEqual(2.*5.-10., self.variable, msg='variable not equal to 2*5-10')



if __name__ == '__main__':
    unittest.main()
