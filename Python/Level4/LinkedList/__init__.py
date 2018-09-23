class Node:
    def __init__(self, v):
        self.val = v
        self.next = None

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))


class DoublyNode:
    def __init__(self, v):
        self.val = v
        self.next = None
        self.prev = None


class Traverse:
    def print_list(self, head):
        p = head

        while p is not None:
            print(p.val, end="->")
            p = p.next
