# SPDX-License-Identifier: MPL-2.0
#
# Jupytext.py -- jupytext
# Copyright (C) 2024  Jacob Koziej <jacobkoziej@gmail.com>

from SCons.Action import Action
from SCons.Builder import BuilderBase
from SCons.Script.SConscript import SConsEnvironment


def generate(env: SConsEnvironment) -> None:
    if env.Detect('Jupytext'):
        return

    env['JUPYTEXT'] = env.get('JUPYTEXT', 'jupytext')

    builder: BuilderBase = env.Builder(
        action=Action(
            '$JUPYTEXT $JUPYTEXTFLAGS --output $TARGET $SOURCE',
            '$JUPYTEXTCOMSTR',
        ),
    )

    env['BUILDERS']['Jupytext'] = builder


def exists(env: SConsEnvironment) -> bool:
    return env.Detect('Jupytext')
