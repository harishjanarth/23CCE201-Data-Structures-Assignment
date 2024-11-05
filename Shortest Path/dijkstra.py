# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 06:25:04 2024

@author: Harish
"""


def dijkstra(graph,source):
    shortest = {vertex:float('inf') for vertex in graph}
    shortest[source] = 0
    
    visited = set()
    
    while len(visited) < len(graph):
        curr = None
        curr_distance = float('inf')
        
        for vertex in graph:
            if vertex not in visited and shortest[vertex] < curr_distance:
                curr = vertex
                curr_distance = shortest[vertex]
            
        if curr == None:
            break
        
        visited.add(curr)
        
        for neighbour,weight in graph[curr]:
            distance = curr_distance + weight
            
            if distance < shortest[neighbour]:
                shortest[neighbour] = distance
        
    return shortest
            
    

def user_input():
    graph = {}
    n = int(input("Enter the number of vertices: "))
    
    for i in range(n):
        vertex = input("\nEnter the vertex: ")
        neighbours = []
        m = int(input(f"Enter the number of edges for {vertex}: "))
        
        for i in range(m):
            neighbour = input(f"Enter neighbour of the {vertex}: ")
            weight = int(input(f"Enter weight for edge {vertex} -> {neighbour}: "))
            neighbours.append((neighbour,weight))
        
        graph[vertex] = neighbours
        
    return graph

def print_graph(graph):
    print("\nGraph Representation:")
    for vertex, neighbours in graph.items():
        for neighbour, weight in neighbours:
            print(f"{vertex} -> {neighbour} (weight: {weight})")

    


graph = user_input()
print_graph(graph)
source = input("Enter the source node: ")
shortest = dijkstra(graph, source)
print("Shortest paths from node", source, ":", shortest)

