# SPDX-License-Identifier: MPL-2.0
#
# Papermill.py -- papermill
# Copyright (C) 2024  Jacob Koziej <jacobkoziej@gmail.com>

from SCons.Action import Action
from SCons.Builder import BuilderBase
from SCons.Script.SConscript import SConsEnvironment


def generate(env: SConsEnvironment) -> None:
    if env.Detect('Papermill'):
        return

    env['PAPERMILL'] = env.get('PAPERMILL', 'papermill')

    builder: BuilderBase = env.Builder(
        action=Action(
            '$PAPERMILL $PAPERMILLFLAGS --cwd ${SOURCE.dir} $SOURCE $TARGET',
            '$PAPERMILLCOMSTR',
        ),
    )

    env['BUILDERS']['Papermill'] = builder


def exists(env: SConsEnvironment) -> bool:
    return env.Detect('Papermill')
