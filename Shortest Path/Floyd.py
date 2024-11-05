def floyd(graph):
    n = len(graph)
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]
    
    for i in range(n):
        dist[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    return dist

def print_matrix(matrix):
    n = len(matrix)
    print("\n\nShortest distances between every pair of vertices:")
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == float('inf'):
                print("inf", end="  ")
            else:
                print(f"{matrix[i][j]:<3}", end="  ")
        print()
        
def print_adjacency_matrix(graph):
    n = len(graph)
    print("\nAdjacency Matrix:")
    for i in range(n):
        for j in range(n):
            if graph[i][j] == float('inf'):
                print("inf", end="  ")
            else:
                print(f"{graph[i][j]:<3}", end="  ")
        print()

def user_input():
    n = int(input("Enter the number of vertices: "))
    graph = [[float('inf') for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        graph[i][i] = 0  
        
    vertex_map = {}
    for i in range(n):
        vertex = input("Enter the vertex: ")
        vertex_map[vertex] = i
    
    for vertex, i in vertex_map.items():
        m = int(input(f"Enter the number of edges for vertex {vertex}: "))
        for _ in range(m):
            neighbor = input(f"Enter neighbour of vertex {vertex}: ")
            weight = int(input(f"Enter weight for edge {vertex} -> {neighbor}: "))
            
            if neighbor in vertex_map:
                j = vertex_map[neighbor]
                graph[i][j] = weight

    return graph

graph = user_input()
print_adjacency_matrix(graph)
distances = floyd(graph)
print_matrix(distances)
