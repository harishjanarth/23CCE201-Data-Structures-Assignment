# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 23:02:58 2024

@author: Harish
"""

def shortest_paths_to_destination(graph, destination):
    
    distances = {vertex: float('inf') for vertex in graph}
    distances[destination] = 0  # Cost to reach the destination from itself is 0
    
   
    updated = True
    while updated == True:  
        updated = False
        
        for vertex in graph:
            for neighbor, weight in graph[vertex]:
                if distances[neighbor] + weight < distances[vertex]:
                    distances[vertex] = distances[neighbor] + weight
                    updated = True

    return distances

def user_input():
    graph = {}
    n = int(input("Enter the number of vertices: "))
    
    for i in range(n):
        vertex = input("\nEnter the vertex: ")
        neighbours = []
        m = int(input(f"Enter the number of edges for {vertex}: "))
        
        for j in range(m):
            neighbour = input(f"Enter neighbour of {vertex}: ")
            weight = int(input(f"Enter weight for edge {vertex} -> {neighbour}: "))
            neighbours.append((neighbour, weight))
        
        graph[vertex] = neighbours
    
    return graph

def print_distances(distances, destination):
    print(f"\nShortest distances to the destination vertex '{destination}':")
    for vertex, distance in distances.items():
        if distance == float('inf'):
            print(f"{vertex} -> No path")
        else:
            print(f"{vertex} -> {distance}")

# Main execution
graph = user_input()
destination = input("Enter the destination node: ")
distances = shortest_paths_to_destination(graph, destination)
print_distances(distances, destination)
