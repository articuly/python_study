# coding:utf-8
class Node:
    def __init__(self, value=None, next=None):
        self.value, self.next = value, next


class Linkedlist:
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self.length = 0
        self.tailnode = None

    def __len__(self):
        return self.length

    def iter_node(self):
        curnode = self.root.next
        while curnode is not self.tailnode:
            yield curnode
            curnode = curnode.next
        yield curnode  # 最后一个节点返回出来

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def append(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('full of linkedlist')
        node = Node(value)
        tailnode = self.tailnode
        if tailnode is None:
            self.root.next = node
        else:
            tailnode.next = node
        self.tailnode = node  # 更新尾部指针
        self.length += 1

    def pop(self):
        if self.root.next is None:
            raise Exception('pop from empty linkedlist')
        curnode = self.root.next
        while curnode.next.next is not None:
            curnode = curnode.next
        node = curnode.next
        value = node.value
        curnode.next = None
        self.tailnode = curnode
        self.length -= 1
        return value

    def appendleft(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('full of linkedlist')
        headnode = self.root.next
        node = Node(value)
        self.root.next = node
        node.next = headnode
        self.length += 1

    def popleft(self):
        if self.root.next is None:
            raise Exception('pop from empty linkedlist')
        headnode = self.root.next
        self.root.next = headnode.next
        value = headnode.value
        self.length -= 1
        del headnode
        return value

    def remove(self, value):  # O(n)
        prenode = self.root
        curnode = self.root.next
        for curnode in self.iter_node():
            if curnode.value == value:
                prenode.next = curnode.next
                del curnode
                self.length -= 1
            else:
                prenode = curnode
        return None  # 表示删除失败

    def find(self, value):  # O(n)
        index = 0
        for node in self.iter_node():
            if node.value == value:
                return index
            index += 1
        return None

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0


def test_Linkedlist():
    ll = Linkedlist()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    assert len(ll) == 5
    assert ll.find(2) == 1
    assert ll.find(0) is None
    ll.remove(1)
    assert len(ll) == 4
    assert ll.find(2) == 0
    assert list(ll) == [2, 3, 4, 5]
    ll.appendleft(-1)
    assert list(ll) == [-1, 2, 3, 4, 5]
    assert ll.popleft() == -1
    assert ll.pop() == 5
    assert ll.tailnode.value == 4
    assert list(ll) == [2, 3, 4]
    ll.clear()
    assert len(ll) == 0
