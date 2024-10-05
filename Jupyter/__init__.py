# SPDX-License-Identifier: MPL-2.0
#
# __init__.py -- Jupyter
# Copyright (C) 2024  Jacob Koziej <jacobkoziej@gmail.com>

from . import ObjCopy

from SCons.Script.SConscript import SConsEnvironment


def generate(env: SConsEnvironment) -> None:
    ObjCopy.generate(env)


def exists(env: SConsEnvironment) -> bool:
    exists: bool = True

    exists &= ObjCopy.exists(env)

    return exists
