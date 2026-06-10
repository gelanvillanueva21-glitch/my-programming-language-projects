class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

def findLowest(head):
    minVal = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data < minVal:
            minVal = currentNode.data
        currentNode = currentNode.next
    return minVal

def removeNode(head, targetNode):
    if head == targetNode:
        return head.next
    currentNode = head
    while currentNode.next and currentNode.next != targetNode:
        currentNode = currentNode.next
    if currentNode.next is None:
        return head
    currentNode.next = currentNode.next.next
    return head

def insertNode(head, newNode, position):
    if position == 1:
        newNode.next = head
        return newNode
    currentNode = head
    for _ in range(position - 2):
        if currentNode.next is None:
            break
        currentNode = currentNode.next
    newNode.next = currentNode.next
    currentNode.next = newNode
    return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverseAndPrint(node1)
print(findLowest(node1))

newNode = Node(98)
node1 = insertNode(node1, newNode, 4)
traverseAndPrint(node1)