import anytree
from anytree import Node,RenderTree

Root = Node("8,0,0")

def NextState(currentState):
    x = []
    for i in currentState.split(","):
        x.append(int(i))
    
    
    

def BFS(tree):
    