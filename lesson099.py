class My_object():
    a = True

obj1 = My_object()
obj2 = obj1

print(obj1)
obj1.a = 'booya'
print(obj1.a)
print(hex(id(obj1)))
print()

print(obj2)
print(obj2.a)
print(hex(id(obj2)))


