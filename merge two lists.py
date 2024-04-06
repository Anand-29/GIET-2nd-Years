class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def insertEnd(self,head,data):
        newNode=Node(data)
        if(head==None):
            head=newNode
            return head
        else:
            temp=head
            while(temp.next!=None):
                temp=temp.next
            temp.next=newNode
            return head
    def display(self,head):
        temp=head
        while(temp!=None):
            print(temp.data,end=" ")
            temp=temp.next
    def merge(self,i,j,k):
        while(i!=None and j!=None):
            if(i.data<j.data):
                k=ob.insertEnd(k,i.data)
                i=i.next
            else:
                k=ob.insertEnd(k,j.data)
                j=j.next
        while(i!=None):
            k=ob.insertEnd(k,i.data)
            i=i.next
        while(j!=None):
            k=ob.insertEnd(k,j.data)
            j=j.next
        return k
        
ob=LinkedList()
head1=None
head2=None
head3=None
print("Enter list 1 data")
list=input().split()
for i in list:
    head1=ob.insertEnd(head1,i)
print("Enter list 2 data")
list=input().split()
for i in list:
    head2=ob.insertEnd(head2,i)
head3=ob.merge(head1,head2,head3)
ob.display(head3)
'''


l1=[2,3,10,15,20];l2=[1,4,11,12]
l3=[]
i,j=0,0
while(i<len(l1) and j<len(l2)):
    if(l1[i]<l2[j]):
        l3.append(l1[i])
        i+=1
    else:
        l3.append(l2[j])
        j+=1
print(*l3)
while(i<len(l1)):
    l3.append(l1[i])
    i+=1
while(j<len(l2)):
    l3.append(l2[j])
    j+=1
print(*l3)'''
















