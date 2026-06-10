
class Tree:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    num_list = []
    helper_Traversal(root, num_list)
    return num_list


def helper_Traversal(root, tmp_list):
    if root is None:
        return tmp_list
    helper_Traversal(root.left, tmp_list)
    tmp_list.append(root.val)
    helper_Traversal(root.right, tmp_list)
    return tmp_list


num1 = Tree(1)
num1.left = Tree(2)
num1.right = Tree(3)
num1.left.left = Tree(5)
num1.left.right = Tree(7)
num1.left.right.left = Tree(9)
num1.right.right = Tree(4)
num_list = inorderTraversal(num1)
print(num_list)
