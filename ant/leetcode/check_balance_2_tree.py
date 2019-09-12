# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        recorde = dict()
        stack = list([None])
        if not root:
            return True
        node = root
        depths = dict()
        while node:
            if node.left and node.left not in recorde:
                stack.append(node)
                node = node.left
                recorde[node] = node
            elif node.right and node.right not in recorde:
                stack.append(node)
                node = node.right
                recorde[node] = node
            else:
                if not node.left and not node.right:
                    depths[node] = 1
                else:
                    left_depth = depths[node.left]  if node.left else 0
                    right_depth = depths[node.right] if node.right else 0
                    if left_depth - right_depth > 1 or right_depth -left_depth >1 :
                        return False
                    depths[node] = max(left_depth, right_depth) + 1
                node = stack.pop()
        return True