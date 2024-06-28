# SPDX-License-Identifier: MPL-2.0
#
# __init__.py -- Binutils
# Copyright (C) 2024  Jacob Koziej <jacobkoziej@gmail.com>

from . import ObjCopy


def generate(env):
    ObjCopy.generate(env)


def exists(env):
    exists = True

    exists &= ObjCopy.exists(env)

    return exists
