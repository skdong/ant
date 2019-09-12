"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        node = root
        query = list()
        nodes = list()
        counter = dict()
        while node:
            if node not in counter:
                counter[node] = 0
                nodes.append(node.val)

            if counter[node] < len(node.children):
                query.append(node)
                counter[node] += 1
                node = node.children[counter[node] - 1]
                query.append(node)
            else:
                node = None
                if query:
                    node = query.pop()
        return nodes