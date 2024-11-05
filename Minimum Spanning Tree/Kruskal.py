# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 17:08:30 2024

@author: Harish
"""

class DisjointSet:
    def __init__(self, vertices):
       
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal(vertices, edges):
    mst = []
    total_cost = 0
    
    edges.sort()
    
    ds = DisjointSet(vertices)
    
    for weight, u, v in edges:
        if ds.find(u) != ds.find(v):
            mst.append((u, v, weight))   
            total_cost += weight
            ds.union(u, v)               
    
    return mst, total_cost

def user_input():
    edges = []
    vertices = set()
    
    n = int(input("Enter the number of vertices: "))
    for i in range(n):
        vertex = input("Enter the vertex: ")
        vertices.add(vertex)
        
    m = int(input("\nEnter the number of edges: "))
    for j in range(m):
        vertex1 = input("\nEnter the first vertex of the edge: ")
        vertex2 = input("Enter the second vertex of the edge: ")
        weight = int(input(f"Enter the weight for edge {vertex1}-{vertex2}: "))
        
        if vertex1 in vertices and vertex2 in vertices:
            edges.append((weight, vertex1, vertex2))
        else:
            print("Vertex doesn't exist in graph")

    return vertices, edges


vertices, edges = user_input()
mst, total_cost = kruskal(vertices, edges)


print("\nMinimum Spanning Tree edges:")
for edge in mst:
    print(f"{edge[0]} - {edge[1]} with weight {edge[2]}")

print(f"\nTotal cost of Minimum Spanning Tree: {total_cost}")
