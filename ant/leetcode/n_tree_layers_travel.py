"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        nodes = [root]
        layers = []
        while nodes:
            layer = list()
            childrens = list()
            for node in nodes:
                if node:
                    layer.append(node.val)
                    childrens.extend(node.children)
            nodes = childrens
            if layer:
                layers.append(layer)
        return layers