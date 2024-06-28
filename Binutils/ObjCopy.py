# SPDX-License-Identifier: MPL-2.0
#
# ObjCopy.py -- objcopy
# Copyright (C) 2024  Jacob Koziej <jacobkoziej@gmail.com>

import SCons


def generate(env):
    if env.Detect('ObjCopy'):
        return

    env['OBJCOPY'] = env.get('OBJCOPY', 'objcopy')

    builder = env.Builder(
        action=SCons.Action.Action(
            '$OBJCOPY $OBJCOPYFLAGS $SOURCE $TARGET',
            '$OBJCOPYCOMSTR',
        ),
    )

    env['BUILDERS']['ObjCopy'] = builder


def exists(env):
    return env.Detect('ObjCopy')
