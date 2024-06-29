# SPDX-License-Identifier: MPL-2.0
#
# Phony.py -- phony target
# Copyright (C) 2024  Jacob Koziej <jacobkoziej@gmail.com>

from typing import Any

from SCons.Node.Alias import Alias
from SCons.Script.SConscript import SConsEnvironment


def Phony(env: SConsEnvironment, target: Any, action: Any) -> list[Alias]:
    return env.AlwaysBuild(env.Alias(target, [], action))


def generate(env: SConsEnvironment) -> None:
    if env.Detect('Phony'):
        return

    env.AddMethod(Phony, 'Phony')


def exists(env: SConsEnvironment) -> bool:
    return env.Detect('Phony')
