class Node:
    # n_node = Next node
    def __init__(self, data=None, n_node=None):
        self.data = data
        self.next = n_node

    def is_tail(self):
        if self.next is None:
            return True
        else:
            return False
