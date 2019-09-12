# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        left_stack = list([None])
        left_recorde = dict()
        right_stack = list([None])


        if not root:
            return True
        if not root.left and not root.right:
            return True
        elif root.left and root.right:
            left_node = root.left
            right_node = root.right
        else:
            return False

        while left_node:
            if left_node.val != right_node.val:
                return False
            if left_node.left and not right_node.right:
                return False
            if not left_node.left and right_node.right:
                return False
            if left_node.right and not right_node.left:
                return False
            if not left_node.right and right_node.left:
                return False

            if left_node.left and left_node.left not in left_recorde:
                left_stack.append(left_node)
                left_node = left_node.left
                left_recorde[left_node] = left_node

                right_stack.append(right_node)
                right_node = right_node.right

            elif left_node.right and left_node.right not in left_recorde:
                left_stack.append(left_node)
                left_node = left_node.right
                left_recorde[left_node] = left_node

                right_stack.append(right_node)
                right_node = right_node.left
            else:
                left_node = left_stack.pop()

                right_node = right_stack.pop()
        return True

    def isSymmetric_stack(self, root):
        tree_stack = list()

        if not root:
            return True
        tree_stack.append((root.left, root.right))
        while tree_stack:
            left, right = tree_stack.pop()
            if not left and not right:
                continue
            elif not left or not right:
                return False
            elif left.val != right.val:
                return False
            tree_stack.append((left.right, right.left))
            tree_stack.append((left.left, right.right))
        return True