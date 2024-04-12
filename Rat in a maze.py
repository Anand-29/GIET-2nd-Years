def safe(list,x,y):
    if(x>=0 and x<=3 and y>=0 and y<=3 and list[x][y]==1):
        return True
    return False
def solution(list,sol,x,y):
    if(x==3 and y==3 and list[x][y]==1):
        sol[x][y]='*'
        return True
    if(safe(list,x,y)==True):
        sol[x][y]='*'
        if(solution(list,sol,x,y+1)==True):
            return True
        if(solution(list,sol,x+1,y)==True):
            return True
        sol[x][y]=0
    return False
#Rat in a Maze
list=[[1,1,1,1],
      [1,0,0,1],
      [1,1,1,1],
      [0,0,1,1]]
sol=[[0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0]]
solution(list,sol,0,0)
for i in range(0,4):
    for j in range(0,4):
        print(sol[i][j],end=" ")
    print()
