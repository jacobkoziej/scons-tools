# SPDX-License-Identifier: MPL-2.0
#
# __init__.py -- my SCons tools
# Copyright (C) 2024  Jacob Koziej <jacobkoziej@gmail.com>

from . import Phony


def generate(env):
    Phony.generate(env)


def exists(env):
    exists = True

    exists &= Phony.exists(env)

    return exists
