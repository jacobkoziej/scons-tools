# SPDX-License-Identifier: MPL-2.0
#
# Phony.py -- phony target
# Copyright (C) 2024  Jacob Koziej <jacobkoziej@gmail.com>


def Phony(env, target, action):
    return env.AlwaysBuild(env.Alias(target, [], action))


def generate(env):
    if env.Detect('Phony'):
        return

    env.AddMethod(Phony, 'Phony')


def exists(env):
    return env.Detect('Phony')
