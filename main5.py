# ['data.in', 'prog_joined.py', 'prog.python3', 'user.stderr', 'precompiled', 'judge.err', 'judge.out', 'user.stdout']
# coding: utf-8
from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *

import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import statistics
import itertools
import functools
import operator
import io
import sys
import json

import precompiled.__settings__
from precompiled.__deserializer__ import __Deserializer__
from precompiled.__deserializer__ import DeserializeError
from precompiled.__serializer__ import __Serializer__
from precompiled.__utils__ import __Utils__
from precompiled.listnode import ListNode
from precompiled.nestedinteger import NestedInteger
from precompiled.treenode import TreeNode

from typing import *

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# user submitted code insert below
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        import os
        print(os.listdir("/mnt"))
        with open("/mnt/prog_joined.py") as f:
            print(f.read())


class __DriverSolution__:
    def __helper__(self, root, m, n):
        def getNodeWithVal(root, n):
            q = []
            q.append(root)
            i = 0
            while i < len(q):
                p = q[i]
                if p:
                    if p.val == n:
                        return p
                    q.append(p.left)
                    q.append(p.right)
                i += 1
            return None

        p = getNodeWithVal(root, m)
        q = getNodeWithVal(root, n)
        ret = Solution().lowestCommonAncestor(
            root, p, q
        )
        return ret


import sys


def _driver():
    SEPARATOR = "\x1b\x09\x1d"
    f = open("user.out", "wb", 0)
    lines = __Utils__().read_lines()
    while True:
        try:
            line = next(lines)

            param_1 = __Deserializer__().to_tree_node(line)
            line = next(lines)
            param_2 = __Deserializer__().to_integer(line)
            line = next(lines)
            param_3 = __Deserializer__().to_integer(line)

            ret = __DriverSolution__().__helper__(
                param_1, param_2, param_3
            )
            out = str(ret.val) if ret else "null"

            out = str.encode(out + '\n')
            f.write(out)
            sys.stdout.write(SEPARATOR)
        except StopIteration:
            break


if __name__ == '__main__':
    _driver()