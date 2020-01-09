# coding:utf-8
class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value, self.next, self.prev = value, next, prev


class Cycle_Double_Linkedlist:
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.next, node.prev = node, node
        self.root = node
        self.length = 0

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def __len__(self):
        return self.length

    def iter_node(self):
        if self.root.next is self.root:
            return
        else:
            curnode = self.headnode()
        while curnode.next is not self.root:
            yield curnode
            curnode = curnode.next
        yield curnode

    def iter_node_reverse(self):
        if self.root.next is self.root:
            return
        else:
            curnode = self.tailnode()
        while curnode.prev is not self.root:
            yield curnode
            curnode = curnode.prev
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def append(self, value):  # O(1), 你发现一般不用 for 循环的就是 O(1)，有限个步骤
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('full of circle double linkedlist')
        node = Node(value=value)
        tailnode = self.tailnode() or self.root
        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('full of circle double linkedlist')
        node = Node(value=value)
        if self.root.next is self.root:
            node.next = self.root
            node.prev = self.root
            self.root.next = node
            self.root.prev = node
        else:
            node.next = self.headnode()
            node.prev = self.root
            self.root.next = node
            self.headnode().prev = node
        self.length += 1

    def remove(self, node):  # O(1)，传入node 而不是 value 我们就能实现 O(1) 删除
        if node is self.root:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1


def test_Cycle_double_linkedlist():
    cdll = Cycle_Double_Linkedlist()
    assert len(cdll) == 0
    cdll.append(1)
    cdll.append(2)
    cdll.append(3)
    assert list(cdll) == [1, 2, 3]
    assert [node.value for node in cdll.iter_node()] == [1, 2, 3]
    assert [node.value for node in cdll.iter_node_reverse()] == [3, 2, 1]
    assert cdll.headnode().value == 1
    cdll.remove(cdll.headnode())
    assert len(cdll) == 2
    assert [node.value for node in cdll.iter_node()] == [2, 3]
    cdll.appendleft(0)
    assert [node.value for node in cdll.iter_node()] == [0, 2, 3]
