# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: main4.py
# Compiled at: 2022-11-18 12:36:07
# Size of source mod 2**32: 901 bytes


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __hash__(self):
        return hash((self.val, self.left, self.right))

    def __eq__(self, other):
        return (
         self.val, self.left, self.right) == (other.val, other.left, other.right)

    def __repr__(self):
        return 'hello, world'


root = TreeNode(5)
root.left = TreeNode(6)
root.right = TreeNode(2)
# okay decompiling __pycache__\main4.cpython-38.pyc
