# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def show(self):
        node = self
        nodes = list()
        while node:
            if node.left:
                nodes.append(node)
                node = node.left
            else:
                print node.val
                if node.right:
                    node = node.right
                else:
                    if nodes:
                        while nodes:
                            node = nodes.pop()
                            print node.val
                            if node.right:
                                node = node.right
                                break
                    else:
                        node = None


def list_trans_tree(tree):
    nodes = dict()
    for i in range(len(tree)):
        if tree[i] == None:
            continue
        if not i in nodes:
            nodes[i] = TreeNode(tree[i])
        node = nodes[i]
        try:
            if tree[i*2+1] != None:
                node.left = TreeNode(tree[i*2+1])
                nodes[i*2+1] = node.left
            if tree[i*2+2] != None:
                node.right = TreeNode(tree[i*2+2])
                nodes[i*2+2] = node.right
        except IndexError:
            break
    return nodes[0]


def prex_oder_to_tree(nodes):
    stack = list()
    root = TreeNode(nodes[0])
    stack.append(root)
    for i in range(len(nodes)/2+1):
        if i*2+1 > len(nodes) -1:
            break
        try:
            left, right = nodes[i*2+1], nodes[i*2+2]
        except IndexError:
            left = nodes[i*2+1]
            right = None
        father = stack.pop(0)
        if left:
            left_node = TreeNode(left)
            father.left = left_node
            stack.append(left_node)
        if right:
            right_node = TreeNode(right)
            father.right = right_node
            stack.append(right_node)
    return root

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        tree = p
        other = q
        tree_stack = list()
        other_stack = list()
        while tree and other:
            if tree.val != other.val:
                return False
            elif tree.left and other.left:
                tree_stack.append(tree)
                other_stack.append(other)
                tree = tree.left
                other = other.left
            elif not tree.left and not other.left:
                if tree.right and other.right:
                    tree = tree.right
                    other = other.right

                elif not tree.right and not other.right:
                    tree = None
                    other = None
                    while tree_stack and other_stack:
                        tree = tree_stack.pop()
                        other = other_stack.pop()
                        if tree.right and other.right:
                            tree = tree.right
                            other = other.right
                            break
                        elif not tree.right and not other.right:
                            tree = None
                            other = None
                            continue
                        else:
                            return False
                else:
                    return False
            else:
                return False
        if tree or other:
            return False
        return True

case = (
[0,1],
[0,1]
)
case1 = (
[12,None,-60],
[12,None,72]
)

case2 = (
[68,41,None,-85,None,-73,-49,-98,None,None,None,-124],
[68,41,None,-85,None,-73,-49,-98,None,None,None,-124]
)
case3 = (
[1,2,3],
[1,2,3]
)
tree, other = prex_oder_to_tree(case3[0]), prex_oder_to_tree(case3[1])
print Solution().isSameTree(tree, other)
