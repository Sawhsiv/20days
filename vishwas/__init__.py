class Node:
    def __init__(self,data = None,next = None) -> None:
        self.__data,self.__next = data,next
    def set_data(self,data):
        self.__data = data
        return self
    def set_next(self,next):
        self.__next = next
        return self
    
    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next
    
    def __str__(self) -> str:
        return f'data:{self.__data}'

class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def insert_at_first(self,data = None):
        if self.head:
            self.head = Node(data,self.head)
        else:
            self.head = self.tail = Node(data)
        self.len += 1
    
    def insert_at_end(self,data):
        if self.tail:
            self.tail.set_next(Node(data))
            self.tail = self.tail.get_next()
        else:
            self.head = self.tail = Node(data)
        self.len += 1
    
    
    
    def __str__(self):
        if self.head:
            temp = self.head
            a = []
            while temp!=None:
                a.append(temp.get_data())
                temp = temp.get_next()
            return f'{a}'
        else:
            return f'{None}'    
    
    def __len__(self):
        return self.len
    
list = LinkList()
while True:
    match input('1.Insert Node at First 2.Insert Node at End 3.Display 4.Exit\nEnter yout choice : '):
        case '1': list.insert_at_first(input("Enter the value : "))
        case '2': list.insert_at_end(input("Enter the value : "))
        case '3': print(list)
        case _: break