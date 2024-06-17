class Node:
    def __init__(self,data) :
        self.data=data
        self.next=None
class hd:
    def __init__(self):
        self.head=None

    def insertb(self,dat):
        nn=Node(dat)
        nn.next=self.head
        self.head=nn

    def insertl(self,dat):
        nl=Node(dat)
        temp=self.head
        while temp.next:
            temp=temp.next 
        temp.next=nl     

    def insertm(self,dat,pos):
        nm=Node(dat)
        temp=self.head
        for i in range(pos):
            temp=temp.next
        nm.next=temp.next
        temp.next=nm

    def delfrb(self):
        temp=self.head
        self.head=temp.next
        temp.next=None

    def delfrl(self):
        temp=self.head.next
        res=self.head
        while(temp.next):
            temp=temp.next
            res=res.next
        res.next=None 
    def delfem(self,pos):
        temp=self.head.next
        res=self.head
        for i in range(pos):
            temp=temp.next
            res=res.next
        res.next=temp.next
        temp.next=None           


    def disp(self):    
        if self.head==None:
            print("lit is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,'->')  
                temp=temp.next                        
x=hd()
d=Node(10)
x.head=d
d1=Node(20)
d.next=d1
d2=Node(30)
d1.next=d2
x.insertm(15,0)
x.insertb(2)
x.insertb(5)
x.insertl(40)
x.insertl(50)
x.delfrb()
x.delfrb()
x.delfrl()
x.delfem(0)
x.disp()