from .node import Node


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # count the number of nodes
    def count(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next
        return count

    def is_empty(self):
        return not bool(self.head)

    # find the node with maximum value
    def max(self):
        if self.head is None:
            raise Exception("Empty List")

        if self.head.is_tail():
            return self.head.data

        to_return = self.head.data
        current = self.head
        while current is not None:
            if current.data > to_return:
                to_return = current.data
            current = current.next

        return to_return

    # find the node with minimum value
    def min(self):
        if self.head is None:
            raise Exception("Empty List")

        if self.head.is_tail():
            return self.head.data

        to_return = self.head.data
        current = self.head
        while current is not None:
            if current.data < to_return:
                to_return = current.data
            current = current.next

        return to_return

    # return the tail node
    def get_tail(self):
        if self.head is None:
            raise Exception("Empty List")

        current = self.head
        while not current.is_tail():
            current = current.next

        return current

    # insert at the end
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while not current.is_tail():
                current = current.next
            current.next = Node(data)

    # insert at the beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # delete the tail node
    def pop(self):
        to_return = None
        if self.head is None:
            raise Exception("Empty List")
        elif self.head.is_tail():
            to_return = self.head.data
            self.head = None
        else:
            current = self.head
            while not current.next.is_tail():
                current = current.next
            to_return = current.next.data
            current.next = None
        return to_return

    # delete the head node
    def pop_left(self):
        if self.head is None:
            raise Exception("Empty List")
        else:
            to_return = self.head.data
            self.head = self.head.next
            return to_return

    def delete(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current is None:
                raise Exception("Number not found")
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next

        if found:
            if previous is None:
                self.head = current.next
            else:
                previous.next = current.next

    # convert into a list
    def to_list(self, reverse=False):
        list = []
        current = self.head
        while current is not None:
            if reverse:
                list.insert(0, current.data)
            else:
                list.append(current.data)
            current = current.next
        return list

    # print the list reverse=True to reverse the order
    def print_list(self, reverse=False):
        list = self.to_list(reverse)
        for value in list:
            print("|{}|-->".format(value), end="")
