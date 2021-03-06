#!/usr/bin/env python
#
# test_override_config.py
# Test code to override default config location
#
# Copyright (C) 2016  Gregory M. Green
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

from __future__ import print_function, division

import unittest

import os
import sys


class TestConfig(unittest.TestCase):
    def test_config_override(self):
        """
        Test overriding default config location.
        """
        # Set the environment variable DUSTMAPS_CONFIG_FNAME
        test_dir = os.path.dirname(os.path.realpath(__file__))
        os.environ['DUSTMAPS_CONFIG_FNAME'] = os.path.join(test_dir, 'test_config.json')

        # Reset the dustmaps.config module
        if 'dustmaps.config' in sys.modules:
            print('Unloading config module ...')
            del sys.modules['dustmaps.config']
        from ..config import config

        # Check that the data directory has been loaded from the test config file
        self.assertEqual(config['data_dir'], '/my/very/special/path')

        # Reset the dustmaps.config module, in case other tests need it
        del os.environ['DUSTMAPS_CONFIG_FNAME']
        del sys.modules['dustmaps.config']
        from ..config import config


if __name__ == '__main__':
    unittest.main()
