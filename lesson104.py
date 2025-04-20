from traceback import print_list

from lesson100 import my_linked_list


class Linked_List:
    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None
        }
        self.tail = self.head
        self.length = 1

    def append(self, value):
        newNode = {
            'value': value,
            'next': None
        }
        self.tail['next'] = newNode
        self.tail = newNode
        self.length += 1
        return self

    def prepend(self, value):
        newNode = {
            'value': value,
            'next': None
        }
        newNode['next'] = self.head
        self.head = newNode
        self.length += 1
        return self

    def print_list(self):
        li = []
        current_node = self.head
        while current_node != None:
            li.append(current_node['value'])
            current_node = current_node['next']
        return li

    def insert(self, index, value):
        pass


my_linked_list = Linked_List(10)
print(my_linked_list.head['value'])
print(my_linked_list.head['next'])
print('Tail:', my_linked_list.tail)
print('Length:', my_linked_list.length)
my_list = my_linked_list.print_list()
print(my_list)
print()

result = my_linked_list.append(5)
print(result)
print(my_linked_list.head['value'])
print(my_linked_list.head['next'])
print('Tail:', my_linked_list.tail)
print('Length:', my_linked_list.length)
my_list = my_linked_list.print_list()
print(my_list)
print()

result = my_linked_list.append(16)
print(result)
print(my_linked_list.head['value'])
print(my_linked_list.head['next'])
print('Tail:', my_linked_list.tail)
print('Length:', my_linked_list.length)
my_list = my_linked_list.print_list()
print(my_list)
print()

result = my_linked_list.prepend(1)
print(result)
print(my_linked_list.head['value'])
print(my_linked_list.head['next'])
print('Tail:', my_linked_list.tail)
print('Length:', my_linked_list.length)
my_list = my_linked_list.print_list()
print(my_list)
print()

result = my_linked_list.prepend(2)
print(result)
print(my_linked_list.head['value'])
print(my_linked_list.head['next'])
print('Tail:', my_linked_list.tail)
print('Length:', my_linked_list.length)
my_list = my_linked_list.print_list()
print(my_list)
print()

