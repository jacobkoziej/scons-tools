# SPDX-License-Identifier: MPL-2.0
#
# NbConvert.py -- jupyter-nbconvert
# Copyright (C) 2024  Jacob Koziej <jacobkoziej@gmail.com>

from SCons.Action import Action
from SCons.Builder import BuilderBase
from SCons.Script.SConscript import SConsEnvironment


def generate(env: SConsEnvironment) -> None:
    if env.Detect('NbConvert'):
        return

    env['NBCONVERT'] = env.get('NBCONVERT', 'jupyter-nbconvert')

    builder: BuilderBase = env.Builder(
        action=Action(
            '$NBCONVERT $NBCONVERTFLAGS $SOURCE $TARGET',
            '$NBCONVERTCOMSTR',
        ),
    )

    env['BUILDERS']['NbConvert'] = builder


def exists(env: SConsEnvironment) -> bool:
    return env.Detect('NbConvert')
