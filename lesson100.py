
class Linked_List:
    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None
        }
        self.tail = self.head
        self.length = 1

    def append(self, value):
        pass

my_linked_list = Linked_List(10)
print(my_linked_list.head['value'])
print(my_linked_list.head['next'])
print('Tail:', my_linked_list.tail)
print('Length:', my_linked_list.length)
