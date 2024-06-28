# SPDX-License-Identifier: MPL-2.0
#
# __init__.py -- my SCons tools
# Copyright (C) 2024  Jacob Koziej <jacobkoziej@gmail.com>

from . import Binutils
from . import Phony


def generate(env):
    Binutils.generate(env)
    Phony.generate(env)


def exists(env):
    exists = True

    exists &= Binutils.exists(env)
    exists &= Phony.exists(env)

    return exists
