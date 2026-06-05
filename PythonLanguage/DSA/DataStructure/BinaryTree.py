
class Trees:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)


root = Trees("A")
node1 = Trees("C")
node2 = Trees("D")
node3 = Trees("F")
node4 = Trees("H")
node5 = Trees("K")
node6 = Trees("L")
node7 = Trees("M")
node8 = Trees("Z")

root.left = node1
root.right = node3

node1.left = node4
node3.right = node8

node4.left = node6
node4.right = node5
node5.left = node2
node5.right = node7

preOrderTraversal(root)
print("root.right.left.data:", root.left.left.right.data)