class Stack:
    def __init__(self) -> None:
        self.items=[]
    def push(self,data):
        return self.items.append(data)
    def popo(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
s=Stack()
s.push(20)
s.push(30)
s.push(50)
print(s.size())
s.popo()
print(s.items)
