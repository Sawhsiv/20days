class node:
    def __init__(self,data):
        self.value = data
        self.next = None
        
head =node(10)
tail=node(10)

tail.next = node(20)
# ta = node(20)
tail=tail.next

#tail.next = node(30)
# tail = tail.next

# tail.next = node(40)
# tail = tail.next

print(head)
print(tail)
print(head.value)
print(tail.value)
print(head.next)
print(tail.next)