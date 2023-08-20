"""
Implementing tree class and such
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional as opt


@dataclass
class TreeNode:
    """Node of a tree with a value and up to two children"""

    value: opt[int] = None
    left: opt[TreeNode] = None
    right: opt[TreeNode] = None


@dataclass
class Tree:
    """A tree, composed of nodes with up to two children each and a value"""

    root: opt[TreeNode] = None

    def __iter__(self):
        return TreePreorderIter(self.root)


class TreePreorderIter:
    """
    Iteration object used by the class `Tree`
    Serialization of tree who's linear order
    is consistent with graph preorder
    """

    stack: list[TreeNode] = []

    def __init__(self, root):
        if root is not None:
            self.stack = [root]

    def __next__(self):
        if len(self.stack) <= 0:
            raise StopIteration
        # else:
        node = self.stack.pop()

        if node.right is not None:
            self.stack.append(node.right)

        if node.left is not None:
            self.stack.append(node.left)

        return node
