def safe(list,r,c):
    for i in range(c,-1,-1):
        if(list[r][i]!=0):
            return False
    for i,j in zip(range(r,-1,-1),range(c,-1,-1)):
        if(list[i][j]!=0):
            return False
    for i,j in zip(range(r,4),range(c,-1,-1)):
        if(list[i][j]!=0):
            return False
    return True
def solution(matrix,column):
    if(column>=4):
        return True
    for row in range(0,4):
        if(safe(list,row,column)==True):
            matrix[row][column]=1
            if(solution(list,column+1)==True):
                return True
        matrix[row][column]=0
    return False
#Rat in a Maze
list=[[0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0]]
if(solution(list,0)):
    for i in range(0,4):
        for j in range(0,4):
            print(list[i][j],end=" ")
        print()
else:
    print("No possible solution")
