class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None


# creating nodes
s1 = SinglyLinkedList()
s1.head = Node(10)
second = Node(20)
third = Node(30)

# linking nodes
s1.head.next = second
second.next = third

while s1.head is not None:
    print(s1.head.data, "----->", end='')
    s1.head = s1.head.next

a = [1, 2, 3]
b = [1, 2, 3]
print("\n", a is b)
print(a == b)
print(id(a))
print(id(b))