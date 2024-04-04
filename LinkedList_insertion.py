class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insertEnd(self,data):
        newNode=Node(data)
        if(self.head==None):
            self.head=newNode
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=newNode
    def display(self):
        if(self.head==None):
            print("empty list")
            return
        temp=self.head
        while(temp!=None):
            print(temp.data,end="  ")
            temp=temp.next
    def insertFront(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
ob=LinkedList()
'''while(True):
    a=int(input())
    if(a<0):
        break
    ob.insert(a)
ob.display()'''
while(True):
    n=int(input("press 1 to insert at end\n2 to display\n3 to\
    insertFront\nother to delete"))
    if(n==1):
        a=int(input("Enter the data to be inserted\n"))
        ob.insertEnd(a)
        print(a," is inserted")
    elif(n==2):
        print("Elements of LinkedList are:")
        ob.display()
        print()
    elif(n==3):
        a=int(input("Enter the data to be inserted\n"))
        ob.insertFront(a)
        print(a," is inserted")
    else:
        break
        
















