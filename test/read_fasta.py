#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Bio import SeqIO

f = input('文件名：')
ft = input('格式：')

f_list = [sequence.seq for sequence in SeqIO.parse(f, ft)]
print(f_list)
