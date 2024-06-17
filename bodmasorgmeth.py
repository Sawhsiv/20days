class Stack:
    def __init__(self) -> None:
        self.items=[]
    def push(self,data):
        return self.items.append(data)
    def popo(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
e=input()
f=0
s=Stack()
ob='[{('
cb=')}]'
for i in e:
    if i in ob:
        s.push(i)
    if i in cb:
        x = s.pop()
        if x == '(' and i == ')':
            pass
        elif x == '{' and i == '}':
            pass
        elif x == '(' and i == ')':
            pass
        else:
            f = 1
            break      
if (f==0) and s.size()==0:
    print(True)
else:
    print(False)    



  