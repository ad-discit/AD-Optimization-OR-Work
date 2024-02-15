from sys import maxsize 
from itertools import permutations
import time
import matplotlib.pyplot as plt

def travellingSalesmanProblem(graph, s): 
    start_time = time.time()
    # store all vertex apart from source vertex 
    vertex = [] 
    for i in range(len(graph)): 
        if i != s: 
            vertex.append(i) 

    # store minimum weight Hamiltonian Cycle 
    min_path = maxsize 
    next_permutation = permutations(vertex)
    for i in next_permutation:

        # store current Path weight( 
        current_pathweight = 0

        # compute current path weight 
        k = s 
        for j in i: 
            current_pathweight += graph[k][j] 
            k = j 
        current_pathweight += graph[k][s] 

        # update minimum 
        min_path = min(min_path, current_pathweight) 
    end_time = time.time()   
    return min_path, end_time - start_time

# Driver Code 
if __name__ == "__main__":
    time_spent = []
    num_vertices = []

    for v in range(2, 10): 
        num_vertices.append(v)
        # generating a graph matrix with uniform distances (2D)
        graph = [[maxsize if i == j else 10 for j in range(v)] for i in range(v)] #I chose uniform distances equal to 10 
        s = 0
        _, time_taken = travellingSalesmanProblem(graph, s) #I discard the minimum path cost
        time_spent.append(time_taken)
    
    plt.plot(num_vertices, time_spent, marker='o', linestyle='-', color='b')
    plt.xlabel('Number of Cities')
    plt.ylabel('Time Spent (seconds)')
    plt.title('Time Complexity for TSP Algorithm')
    plt.grid(True)
    plt.show()
