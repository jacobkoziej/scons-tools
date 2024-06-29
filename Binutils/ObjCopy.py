# SPDX-License-Identifier: MPL-2.0
#
# ObjCopy.py -- objcopy
# Copyright (C) 2024  Jacob Koziej <jacobkoziej@gmail.com>

from SCons.Action import Action
from SCons.Builder import BuilderBase
from SCons.Script.SConscript import SConsEnvironment


def generate(env: SConsEnvironment) -> None:
    if env.Detect('ObjCopy'):
        return

    env['OBJCOPY'] = env.get('OBJCOPY', 'objcopy')

    builder: BuilderBase = env.Builder(
        action=Action(
            '$OBJCOPY $OBJCOPYFLAGS $SOURCE $TARGET',
            '$OBJCOPYCOMSTR',
        ),
    )

    env['BUILDERS']['ObjCopy'] = builder


def exists(env: SConsEnvironment) -> bool:
    return env.Detect('ObjCopy')
