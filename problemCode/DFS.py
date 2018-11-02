import operator
import numpy as np

x = input("Matrix of 0s and 1s Please : ")

x = np.matrix(x)
print(x)

visited = np.zeros(x.shape,dtype=int)

def possible_list(x,visited,i,j):
    positions = [(-1,-1),(1,-1),(1,1),(-1,1),(0,1),(0,-1),(-1,0),(1,0)]
    possiblepositions = []
    for displ in positions:
        (X,Y) = tuple(map(operator.add, displ, (i,j)))
        if X<0 or X>=x.shape[0] or Y<0 or Y>=x.shape[1]:
            continue
        else:
            possiblepositions.append((X,Y))
    return possiblepositions

def adjecent_1andnonvisited(x,visited,i,j):
    positions = [(-1,-1),(1,-1),(1,1),(-1,1),(0,1),(0,-1),(-1,0),(1,0)]
    possiblepositions = []
    for displ in positions:
        (X,Y) = tuple(map(operator.add, displ, (i,j)))
        if X<0 or X>=x.shape[0] or Y<0 or Y>=x.shape[1]:
            continue
        else:
            possiblepositions.append((X,Y))


    for position in possiblepositions:
        if (x[position[0],position[1]] == 1) and (visited[position[0],position[1]] == 0):
            return position
    return (-1,-1)


def DFS(x,visited,X,Y,length):
    visited[X][Y] = 1
    
    possi = possible_list(x,visited,X,Y)
    print(possi)
    for posiposes in possi:
        (p,q) =adjecent_1andnonvisited(x,visited,X,Y)
        if p!=-1 and q != -1:
            length+=1
            length = DFS(x,visited,p,q,length)
        else:
            return length

maxi = 0

for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        if ((visited[i,j]==0) and (x[i,j]==1)):
            maxi =max(maxi,DFS(x,visited,i,j,1))
            
print(maxi)