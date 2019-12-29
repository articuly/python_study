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
        self.data = new_data


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

    def insert_head(self, node):
        self.length += 1
        self.head, node.next = node, self.head

    def pop_head(self):
        head = self.head
        if self.head is not None:
            self.head = self.head.next
            self.length -= 1
        return head

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
        node, current.next = current.next, None
        self.length -= 1
        return node

    def insert(self, index, new_node):
        if self.head is None or index < 1:
            self.head, new_node.next = new_node, self.head
        else:
            current = self.head
            while index > 1 and current.next is not None:
                current = current.next
                index -= 1
            new_node.next, current.next = current.next, new_node
            self.length += 1

    def remove(self, index):
        if self.head is Node or index < 1:
            return None
        else:
            current = self.head
            if index < len(self):
                while index > 1 and current.next is not None:
                    current = current.next
                    index -= 1
                self.length -= 1
                node, current.next = current.next, current.next.next
                return node
            else:
                raise IndexError('out of index range')


def test_LinkedList():
    import pytest
    ll = LinkedList()
    assert ll.head == None
    for i in range(5):
        node = Node(i)
        ll.insert_head(node)
    assert len(ll) == 5
    assert [node.data for node in ll] == [4, 3, 2, 1, 0]
    ll.append_node(Node('new'))
    assert [node.data for node in ll] == [4, 3, 2, 1, 0, 'new']
    assert ll.pop_end().data == 'new'
    assert [node.data for node in ll] == [4, 3, 2, 1, 0]
    assert ll.pop_head().data == 4
    assert [node.data for node in ll] == [3, 2, 1, 0]
    o = Node('oh!')
    ll.insert(2, o)
    assert [node.data for node in ll] == [3, 2, 'oh!', 1, 0]
    assert ll.remove(3).data == 1
    with pytest.raises(IndexError) as excinfo:
        ll.remove(4)
    assert 'out' in str(excinfo.value)
    a = Node(3, next=Node(2))
    assert a.get_next().data == 2
