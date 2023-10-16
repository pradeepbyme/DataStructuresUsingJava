class Node:
    def __init__(self, data, llink=None, rlink=None):
        self.llink = llink
        self.data = data
        self.rlink = rlink


class DoublyLinkedList:
    def __init__(self):
        self.llink = None
        self.rlink = None


d = DoublyLinkedList()
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# for node1
node1.llink = None
node1.rlink = node2

# for node2
node2.llink = node1
node2.rlink = node3

# for node3
node3.llink = node2
node3.rlink = None

print(node1.data , node1.rlink.data)
