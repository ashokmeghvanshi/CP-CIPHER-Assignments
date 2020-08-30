class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        
def findtopelement(node,distance,level,topelement): 
    if(node==None): 
        return node
      
    if distance not in topelement or topelement[distance][1]>level:
        topelement[distance] = [node.data,level] 
    findtopelement(node.left,distance-1,level+1,topelement)
    findtopelement(node.right,distance+1,level+1,topelement)
  
def topView(root): 
    topelement={} 
    distance=0
    level=0
    findtopelement(root,distance,level,topelement) 
    for i in sorted(topelement.keys()): 
        print(topelement[i][0],end =' ') 
      

from collections import deque
import queue 

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
def make_tree():
    n=int(input())
    l=list(map(str,input().split()))
    head=None
    q=deque()
    i=0
    while(n>0):
        a,b,c=l[i],l[i+1],l[i+2]
        if(not head):
            head=Node(int(a))
            q.append(head)
        pick=q[0]
        q.popleft()
        if(c=='L'):
            pick.left=Node(int(b))
            q.append(pick.left)
        n=n-1
        if(not n):
            break
        a,b,c=l[i+3],l[i+4],l[i+5]
        if(c=='R'):
            pick.right=Node(int(b))
            q.append(pick.right)
        i=i+6
        n=n-1
    return head
            

if __name__ == '__main__':
    t=int(input())
    for _ in range(0,t):
        root=make_tree()
        topView(root)
        print()
