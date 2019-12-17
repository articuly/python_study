# coding:utf-8
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        head = self.head
        while head is not None:
            current, head = head, head.next
            yield current
            # print(current.data)

    def insert_head(self, node):
        self.head, node.next = node, self.head
        self.length += 1

    def pop_head(self):
        head = self.head
        if self.head is not None:
            self.head = self.head.next
        return head
        self.length -= 1

    def append_node(self, node):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node
        self.length += 1

    def pop_end(self):
        current = self.head
        while current.next.next is not None:
            current = current.next
        return current.next
        current.next = None
        self.length -= 1

    def insert(self, index, new_node):
        self.length += 1
        if self.head is None or index < 1:
            self.head, new_node.next = new_node, self.head
        else:
            current = self.head
        while index > 1 and current.next is not None:
            current = current.next
            index -= 1
        current.next, new_node.next = new_node, current.next

    def remove(self, index):
        self.length -= 1
        if self.head is Node or index < 1:
            return None
        else:
            current = self.head
        while index > 1 and current.next is not None:
            current = current.next
            index -= 1
        current.next = current.next.next


ll = LinkedList()
for i in range(10):
    node = Node(i)
    ll.insert_head(node)
print(len(ll))
print([node.data for node in ll])
new_node = Node('new')
ll.append_node(new_node)
print([node.data for node in ll])
d = ll.pop_head()
print(d.data)
e = ll.pop_end()
print(e.data)
print([node.data for node in ll])
ll.insert(3, Node('oh!'))
print([node.data for node in ll])
ll.remove(4)
print([node.data for node in ll])
