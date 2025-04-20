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

my_linked_list = Linked_List(10)
print(my_linked_list.head['value'])
print(my_linked_list.head['next'])
print('Tail:', my_linked_list.tail)
print('Length:', my_linked_list.length)
result = my_linked_list.append(5)
print(result)
print(my_linked_list.head['value'])
print(my_linked_list.head['next'])
print('Tail:', my_linked_list.tail)
print('Length:', my_linked_list.length)
result = my_linked_list.append(16)
print(result)
print(my_linked_list.head['value'])
print(my_linked_list.head['next'])
print('Tail:', my_linked_list.tail)
print('Length:', my_linked_list.length)
