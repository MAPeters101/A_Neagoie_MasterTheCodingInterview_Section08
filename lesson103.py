
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_List:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        self.new_node = Node(value)
        self.tail.next = self.new_node.next
        self.tail = self.new_node
        self.length += 1
        return self

    def prepend(self, value):
        self.new_node = Node(value)
        self.new_node.next = self.head
        self.head = self.new_node
        self.length += 1
        return self


my_linked_list = Linked_List(10)
print(my_linked_list.head.value)
print(my_linked_list.head.next)
print('Tail:', my_linked_list.tail.value)
print('Tail:', my_linked_list.tail.next)
print('Length:', my_linked_list.length)
print()

result = my_linked_list.append(5)
print(result)
print(my_linked_list.head.value)
print(my_linked_list.head.next)
print('Tail:', my_linked_list.tail.value)
print('Tail:', my_linked_list.tail.next)
print('Length:', my_linked_list.length)
print()

result = my_linked_list.append(16)
print(my_linked_list.head.value)
print(my_linked_list.head.next)
print('Tail:', my_linked_list.tail.value)
print('Tail:', my_linked_list.tail.next)
print('Length:', my_linked_list.length)
print()

result = my_linked_list.prepend(1)
print(my_linked_list.head.value)
print(my_linked_list.head.next)
print('Tail:', my_linked_list.tail.value)
print('Tail:', my_linked_list.tail.next)
print('Length:', my_linked_list.length)
print()

result = my_linked_list.prepend(2)
print(my_linked_list.head.value)
print(my_linked_list.head.next)
print('Tail:', my_linked_list.tail.value)
print('Tail:', my_linked_list.tail.next)
print('Length:', my_linked_list.length)
print()


