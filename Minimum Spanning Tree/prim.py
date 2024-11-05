# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 20:08:22 2024

@author: Harish
"""

def user_input():
    graph = {}
    n = int(input("Enter the number of vertices: "))
    
    for i in range(n):
        vertex = input("Enter the vertex: ")
        graph[vertex] = []
        
    m = int(input("\nEnter the number of edges: "))
    for j in range(m):
        vertex1 = input("\nEnter the first vertex of the edge: ")
        vertex2 = input("Enter the second vertex of the edge: ")
        weight = int(input(f"Enter the weight for edge {vertex1}-{vertex2}: "))
        
        if vertex1 in graph and vertex2 in graph:
            graph[vertex1].append((vertex2,weight))
            graph[vertex2].append((vertex1,weight))
        else:
            print("Vertex doesn't exist in graph")
            
    return graph

def prim(graph,source):
    visited = set()
    mst = []
    total_cost = 0
    
    visited.add(source)
    
    edges = [(weight,source,neighbour) for neighbour,weight in graph[source]]
    
    while edges:
        for i in range(len(edges)):
            index = i
            for j in range(i+1,len(edges)):
                if edges[j][0] < edges[index][0]:
                    index = j
            edges[i],edges[index] = edges[index],edges[i]
            
        weight,from_vertex,to_vertex = edges.pop(0)
        
        if to_vertex not in visited:
            visited.add(to_vertex)
            mst.append((from_vertex,to_vertex,weight))
            
            total_cost+=weight
            
            for neighbour,weight in graph[to_vertex]:
                if neighbour not in visited:
                    edges.append((weight,to_vertex,neighbour))
                    
    return mst,total_cost

graph = user_input()
source = input("Enter the source vertex: ")
mst,total_cost = prim(graph,source)

print("\nMinimum Spanning Tree edges:")
for edge in mst:
    print(f"{edge[0]} - {edge[1]} with weight {edge[2]}")

print(f"\nTotal cost of Minimum Spanning Tree: {total_cost}")
        
