#!/usr/bin/python3
import hidden_4 as h

names = dir(hidden_4)
for name in sorted(names):
    if not name.startswith('__'):
        print(name)

