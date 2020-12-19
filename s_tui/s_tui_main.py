#!/usr/bin/python

# Copyright (C) 2017-2020 Alex Manuskin, Gil Tsuker
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
#
# This implementation was inspired by Ian Ward
# Urwid web site: http://excess.org/urwid/

"""CPU stress and monitoring utility"""

from __future__ import absolute_import

import argparse
import signal
import itertools
import logging
import os
import subprocess
import time
import timeit
from collections import OrderedDict
from collections import defaultdict
import sys

import psutil
import urwid

try:
    import configparser
except ImportError:
    import ConfigParser as configparser


def add_path(path):
    if path not in sys.path:
        print('Adding {}'.format(path))
        sys.path.append(path)


abs_current_path = os.path.realpath('./')
root_path = os.path.join('/', *abs_current_path.split(os.path.sep)[:-1])
add_path(root_path)

# Helpers
from s_tui.helper_functions import output_to_terminal
from s_tui.sources.rapl_power_source import RaplPowerSource


def main():
    sources = [RaplPowerSource()]
    output_to_terminal(sources)


if __name__ == '__main__':
    main()
