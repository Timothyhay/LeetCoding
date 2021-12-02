
# Node Class
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

def printlist(node):
    if (node == None):
        return
    while (node != None):
        print(node.data, " -> ", end="")
        node = node.next

def reverselist(head):
    cur = head
    pre = None
    nxt = None
    while (cur != None):
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre


head = None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

printlist(head)  # print original list
head = reverselist(head)
print()
printlist(head)  # print modified list


# Saved Ans

'''def reverselist(node):
    prev = None
    curr = node
    next = None
    while (curr != None):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    node = prev
    return node

'''