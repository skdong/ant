class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        values = list()
        nodes = list()
        overs = list()
        nodes.append(root)
        while nodes:
            node = nodes.pop()
            if not node:
                continue
            overs.append(node)
            if node.left:
                nodes.append(node.left)
            elif node.right:
                nodes.append(node.right)

        return values