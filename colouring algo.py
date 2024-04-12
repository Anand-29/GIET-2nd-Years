def solution(list,oldcolor,newcolor,x,y):
    if(x<0 or x>4 or y<0 or y>4 or list[x][y]!=oldcolor):
        return
    if(list[x][y]==newcolor):
        return
    list[x][y]=newcolor
    solution(list,oldcolor,newcolor,x,y+1)
    solution(list,oldcolor,newcolor,x,y-1)
    solution(list,oldcolor,newcolor,x+1,y)
    solution(list,oldcolor,newcolor,x-1,y)
#Flood or colouring algo
list=[[0,0,1,0,0],
      [0,0,1,0,0],
      [1,1,1,1,1],
      [0,0,1,0,0],
      [0,0,1,0,0]]
oldcolor,newcolor,x,y=1,3,2,2
solution(list,oldcolor,newcolor,x,y)
for i in range(0,5):
    for j in range(0,5):
        print(list[i][j],end=" ")
    print()
      
