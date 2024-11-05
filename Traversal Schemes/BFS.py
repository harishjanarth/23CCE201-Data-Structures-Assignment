# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 21:10:52 2024

@author: Harish
"""

import numpy as np

class Queue:
    def __init__(self,max_size=10):
        self.max_size = max_size
        self.front = -1
        self.rear = -1
        self.queue = np.empty(max_size,dtype=object)
        
    
    def enqueue(self,val):
        if (self.front == 0 and self.rear == self.max_size-1) or (self.rear == self.front-1):
            print("Overflow")
            return
        if self.front == -1:
            self.front=0
            self.rear=0 
        elif self.rear == self.max_size-1 and self.front!=0:
            self.rear=0
        else:
            self.rear+=1    
        self.queue[self.rear] = val
    def dequeue(self):
         if self.front == -1:
             print("Underflow")
             return
         item = self.queue[self.front]
         self.queue[self.front] = None
         
         if self.front == self.rear:
             self.front = -1
             self.rear = -1
        
         elif self.front == self.max_size-1:
             self.front = 0
        
         else:
             self.front+=1
        
         return item
     

def user_input():
    graph = {}
    n = int(input("Enter the number of vertices: "))
    
    for i in range(n):
        vertex = input("\nEnter the vertex: ")
        neighbours = []
        m = int(input(f"Enter the number of edges for {vertex}: "))
        
        for i in range(m):
            neighbour = input(f"Enter neighbour of the {vertex}: ")
            #weight = int(input(f"Enter weight for edge {vertex} -> {neighbour}: "))
            neighbours.append(neighbour)
            
        
        graph[vertex] = neighbours
        
    
    return graph


def bfs_algo(q,bfs,visited):
    while q.front!=-1:
        vertex = q.dequeue()
        bfs.append(vertex)
        
        for i in graph[vertex]:
            if i not in visited:
               visited.add(i)
               q.enqueue(i)

def BFS(graph,source):
    q = Queue()
    q.enqueue(source)
    visited = set()
    visited.add(source)
    
    bfs=[]
    
    bfs_algo(q,bfs,visited)
               
    
    for vertex in graph:
        if vertex not in visited:
            q.enqueue(vertex)
            visited.add(vertex)
            bfs_algo(q,bfs,visited)
                
    return bfs
    
def print_graph(graph):
    print("\nGraph Representation:")
    for vertex, neighbours in graph.items():
        for neighbour in neighbours:
            print(f"{vertex} -> {neighbour}")
      

graph = user_input()
print_graph(graph)
source = input("Enter the source node: ")
bfs = BFS(graph,source)
print(bfs)