class Test:
    public_prop = "public"
    __private_prop = "private"

    def __init__(self, prop1):
        self.prop1 = prop1
        pass
    
print(Test("something").public_prop)

# list 
li = []
li.append(2)
li.extend([1,2])
li2 = li.copy()
print(li[1])
print(li)
del li[1]
print(li)
li.index(1)

li.sort()
li.sort(reverse= True)
li.sort(key=lambda x:x)

# tuple 
tup = (1,2)

# set 
s = {}
s1 = set()
s.add(1)
s.remove(1)

# dict 
hm = {}
hm[1] = 'one'
print(hm[1])
del hm[1]
hm[2] = 'three'
print(hm)

if 1 in hm:
    print("is present")

for key in hm.keys():
    print(key)

# linked list 

class ListNode():

    def __init__(self, val):
        self.val = val
        self.next = None
        pass

# graph

# adj list
graph = {}
edges = [[1,2], [2,3], [4,5]] # directed
for edge in edges:
    if edge[0] in graph:
        graph[edge[0]].append(edge[1])

# bfs 
# dfs 

# heap
import heapq
minheap = []
heapq.heappush(minheap,1)
heapq.heappop(minheap)

maxheap = []
heapq.heappush(maxheap, -1 * 9)
print(-1 * heapq.heappop(maxheap))

# deque
from collections import deque

stack = deque()
stack.append(1)
stack.pop()

q = deque()
q.appendleft(1)
q.pop()

# permu and combi 

import itertools

string = "abca"
print(list(itertools.combinations(string, 2)))
print(list(itertools.permutations(string, 2)))

