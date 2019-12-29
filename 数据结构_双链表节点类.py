# coding:utf-8
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_data(self, new_data):
        self.data = new_data


class Double_LinkedList:
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
        if self.head is not None:
            head = self.head
            self.head = node
            node.next = head
            # node.prev = None  # 默认节点prev为None
            head.prev = node
        else:
            self.head = node

    def pop_head(self):
        head = self.head
        if self.head is not None:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
        return head

    def append_node(self, node):
        if self.head is None:
            self.head = node
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node
        node.prev = current
        # node.next = None  # 默认节点next为None
        self.length += 1

    def pop_end(self):
        current = self.head
        while current.next.next is not None:
            current = current.next
        node, current.next = current.next, None
        node.next, node.prev = None, None  # 断开前后链接
        self.length -= 1
        return node

    def insert(self, index, new_node):
        if self.head is None or index < 1:
            self.head, new_node.next = new_node, self.head
            new_node.prev = None
        else:
            current = self.head
            while index > 1 and current.next is not None:
                current = current.next
                index -= 1
            new_node.next, current.next = current.next, new_node
            new_node.prev = current
            # new_node.next.prev = new_node
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
                current.next.prev = current
                node.next, node.prev = None, None  # 断开前后链接
                return node
            else:
                raise IndexError('out of index range')


def test_Double_LinkedList():
    import pytest
    dll = Double_LinkedList()
    assert dll.head == None
    for i in range(5):
        node = Node(i)
        dll.insert_head(node)
    assert len(dll) == 5
    assert [node.data for node in dll] == [4, 3, 2, 1, 0]
    dll.append_node(Node('new'))
    assert [node.data for node in dll] == [4, 3, 2, 1, 0, 'new']
    assert dll.pop_end().data == 'new'
    assert [node.data for node in dll] == [4, 3, 2, 1, 0]
    assert dll.pop_head().data == 4
    assert [node.data for node in dll] == [3, 2, 1, 0]
    o = Node('oh!')
    dll.insert(2, o)
    assert [node.data for node in dll] == [3, 2, 'oh!', 1, 0]
    assert dll.remove(3).data == 1
    assert [node.data for node in dll] == [3, 2, 'oh!', 0]
    with pytest.raises(IndexError) as excinfo:
        dll.remove(4)
    assert 'out' in str(excinfo.value)
    assert Node('oh!').data == 'oh!'
    a, b, c = Node(3), Node(2), Node(1)
    a.next = b
    b.next = c
    c.prev = b
    b.prev = a
    assert a.next.data == 2
    assert b.prev.data == 3
