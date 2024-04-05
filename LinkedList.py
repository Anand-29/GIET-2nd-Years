class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def size(self,c=0):
        temp=self.head
        while(temp!=None):
            temp=temp.next
            c+=1
        return c
    def insert(self,data,index=-1):
        if(index==-1):
            index=ob.size()
        newNode=Node(data)
        if(self.head==None):
            self.head=newNode
        else:
            temp=self.head
            if(index>0):
                while(index-1>0):
                    if(temp==None):
                        print("Position doesn't exist")
                        return -1
                    temp=temp.next
                    index-=1
                temp2=temp.next
                if(temp2==None):
                    temp.next=newNode
                    return 
                temp.next=newNode
                newNode.next.temp2
    def delete(self,index=-1):
        if(index==-1):
            index=ob.size()
        if(self.head==None):
            print("List is empty")
            return -1
        temp1=self.head
        if(index>0):
            while(index-1>0):
                temp1=temp1.next
                if(temp1==None):
                    print("Position dosen't exist")
                    return -1
                index-=1
            self.head=temp1.next
            del temp1
            return
        self.head=temp.next
        del temp
    def display(self):
        if(self.head==None):
            print("Empty list")
            return
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next
            
ob=LinkedList()
ob.insert(10)
ob.delete(5)
ob.insert(20,5)
ob.delete()
ob.insert(10)
ob.display()
