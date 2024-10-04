# SPDX-License-Identifier: MPL-2.0
#
# __init__.py -- my SCons tools
# Copyright (C) 2024  Jacob Koziej <jacobkoziej@gmail.com>

from . import Binutils
from . import Jupytext
from . import Phony

from SCons.Script.SConscript import SConsEnvironment


def generate(env: SConsEnvironment) -> None:
    Binutils.generate(env)
    Jupytext.generate(env)
    Phony.generate(env)


def exists(env: SConsEnvironment) -> bool:
    exists: bool = True

    exists &= Binutils.exists(env)
    exists &= Jupytext.exists(env)
    exists &= Phony.exists(env)

    return exists
