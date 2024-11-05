# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 21:24:29 2024

@author: Harish
"""

WHITE,GRAY,BLACK = 0,1,2

def dfs_algo(vertex,graph,color):
    color[vertex] = GRAY
    print(vertex,end=" ")
    
    for i in graph[vertex]:
        if color[i] == WHITE:
            dfs_algo(i,graph,color)
            
    color[vertex] = BLACK
    
def dfs(graph,source):
    color = {vertex:WHITE for vertex in graph}
    
    if source in graph and color[source]==WHITE:
        dfs_algo(source, graph, color)
        
    for vertex in graph:
        if color[vertex]==WHITE:
            dfs_algo(vertex, graph, color)
        
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

def print_graph(graph):
    print("\nGraph Representation:")
    for vertex, neighbours in graph.items():
        for neighbour in neighbours:
            print(f"{vertex} -> {neighbour}")
      

graph = user_input()
print_graph(graph)
source = input("Enter the source node: ")
dfs(graph,source)