class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Graph:
    def __init__(self,V):
        self.v=V
        self.graph=[None]*V
    def insert(self,vertex,edge):
        newNode=Node(edge)
        if(self.graph[vertex]==None):
            self.graph[vertex]=newNode
        else:
            temp=self.graph[vertex]
            while(temp.next!=None):
                temp=temp.next
            temp.next=newNode
    def display(self):
        for i in range(0,self.v):
            temp=self.graph[i]
            print("Vertex:- ",i," edges:- ",end=" ")
            while(temp!=None):
                print(temp.data,end=" ")
                temp=temp.next
            print()
    def DFS(self,vertex,visited=[]):
        if(len(visited)==0):
            visited=[False]*self.v
        visited[vertex]=True
        print(vertex,end=" ")
        temp=self.graph[vertex]
        while(temp!=None):
            data=temp.data
            if(visited[data]!=True):
                self.DFS(data,visited)
            temp=temp.next
    def BFS(self,vertex,visited=[]):
        if(len(visited)==0):
            visited=[False]*self.v
        Queue=[]
        Queue.append(vertex)
        while(len(Queue)!=0):
            data=Queue.pop()
            print(data,end=" ")
            temp=self.graph[data]
            while(temp!=None):
                data2=temp.data
                if(visited[data2]!=True):
                    visited[data2]=True
                    Queue.append(data2)
                temp=temp.next
ob=Graph(4)
ob.insert(0,1)
ob.insert(0,2)
ob.insert(1,2)
ob.insert(3,2)
ob.display()
print("DFS:- ");ob.DFS(0);print()
print("BFS:- ");ob.BFS(0)
