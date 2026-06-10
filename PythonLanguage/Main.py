class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def orderTree(root):
    temp_list = []
    if root is None:
        return temp_list
    else:
        print(root.val)
    orderTree(root.left, temp_list)
    temp_list.append(root.val)
    orderTree(root.right, temp_list)
    return temp_list


tree1 = TreeNode(1)
tree1.left = TreeNode(4)
tree1.left.left = TreeNode(5)
tree1.left.right = TreeNode(6)
tree1.right = TreeNode(8)
tree1.right.left = TreeNode(9)
tree1.right.right = TreeNode(7)

print(orderTree(tree1))