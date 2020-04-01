#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

path = input('路径：')
ft = input('格式：')
file_num = 0
for fn in os.listdir(path):
    if fn[-2:] == '.fna':
        file_num += 1
print(file_num)
