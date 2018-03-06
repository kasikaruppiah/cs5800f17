# Uses python3

import sys
from collections import defaultdict

# Algorithm:
#   1. Create a graph with the number of vertices in the first line of user input
#   2. Create an edge with the vertex numbers given as input from the second line of user input and add it to the graph
#   3. Create a DAG of the graph
#       i. Find the SCCs of the graph
#       ii. Collapse the SCCs into vertices and create a new graph containing only edges from the original graph which connects 2 vertices of different SCC
#   4. find the Topological sort order of the DAG
#.  5. starting from the rightmost vertex of the DAG find the maximum nodes that can be traversed from that vertex
#       i. maximum nodes traversed is 1 + (maximum nodes that can be traversed from the connected vertices that have an edge starting from current node)
#   6. return the maximum of all the maximum nodes that can be travesed from all vertices
# Analysis:
#   1. Running Time: O(V + E)
#       Finding SCCs of G: O(V + E)
#       Creating DAG from SCC: O(E)
#       Topological Sort of DAG: O(V + E)
#       Maximum nodes reachable: O(E)
#   2. Space Complexity: O(V + E)
#       Input Graph: O(V + E)
#       DAG: O(V + E)
#       Reachable Array: O(V)
#       Stack: O(V)
#       Visited Array: O(V)

# Class to represent Graphs


class Graph:

    # Constructor for Graph to initialize number of vertices and adjacency list
    def __init__(self, vertices):
        # Set the number of Vertices in the graph
        self.V = vertices
        # Create an empty adjacency list to store edjes
        self.G = defaultdict(set)

    # Add an edje to the adjacency list of the graph
    def addEdge(self, u, v):
        # add the vertex v to the adjacency list of u
        self.G[u].add(v)

    # Return a new graph by reverse the direction of the edjes of the original
    # graph
    def reverseEdges(self):
        # Create a new graph of same size as original graph
        reverseGraph = Graph(self.V)
        # Reverse the direction of edges in graph by traversing the adjacency
        # list and add it to the new graph
        for u in self.G:
            for v in self.G[u]:
                reverseGraph.addEdge(v, u)

        return reverseGraph

    # DFS from the source vertex
    def DFS(self, u, visited, stack):
        # Mark the source as visited
        visited[u] = True
        # Explore all unexplored adjacent vertices to the source vertex
        for v in self.G[u]:
            if visited[v] == False:
                self.DFS(v, visited, stack)
        # add the node to the stack
        stack.append(u)

    # DFS from the source vertex
    def reverseDFS(self, u, visited, scc):
        # Mark the source as visited
        visited[u] = True
        # add the source to the scc
        scc.append(u)
        # Explore all unexplored adjacent vertices to the source vertex
        for v in self.G[u]:
            if visited[v] == False:
                self.reverseDFS(v, visited, scc)

    # find SCCs in the directed graph
    def stronglyConnectedComponents(self):
        self.SCCs = []
        stack = []
        # Mark all nodes as unvisited
        visited = [False] * (self.V + 1)
        for u in range(1, self.V + 1):
            if visited[u] == False:
                self.DFS(u, visited, stack)

        # Reverse the graph
        reverseGraph = self.reverseEdges()
        # Reset visited array values
        visited = [False] * (self.V + 1)

        # Process verteices in stack one at a time
        while stack:
            u = stack.pop()
            if visited[u] == False:
                scc = []
                reverseGraph.reverseDFS(u, visited, scc)
                self.SCCs.append(scc)

    # Returns the scc index of a vertex
    def findSCC(self, u):
        for i in range(len(self.SCCs)):
            if u in self.SCCs[i]:
                return i

    # Returns a new DAG for the directed graph
    def DAG(self):
        # find the SCCs in the graph
        self.stronglyConnectedComponents()
        dag = Graph(len(self.SCCs))
        for u in self.G:
            scc1 = self.findSCC(u)
            for v in self.G[u]:
                scc2 = self.findSCC(v)
                if scc1 != scc2:
                    dag.addEdge(scc1, scc2)

        return dag

    # Util to help topological sort
    def topologicalSortUtil(self, u, visited, stack):
        # Mark the source as visited
        visited[u] = True
        # Explore all unexplored adjacent vertices to the source vertex
        for v in self.G[u]:
            if visited[v] == False:
                self.topologicalSortUtil(v, visited, stack)
        stack.insert(0, u)

    # finds the topological sorted order of the DAG
    def topologicalSort(self):
        stack = []
        visited = [False] * (self.V)

        for u in range(self.V):
            if visited[u] == False:
                self.topologicalSortUtil(u, visited, stack)
        self.TS = stack

    # find the maximum reachable node for all nodes in the graph
    def maxReachable(self):
        self.topologicalSort()
        # initialize all reachable values to 1
        self.reachable = [1] * (self.V)
        for u in reversed(self.TS):
            self.reachable[u] += max(
                [self.reachable[i] for i in self.G[u]], default=0)
        print(max(self.reachable))


if __name__ == '__main__':
    # read user input
    input = sys.stdin.read()
    # split the input to vertices count and rest of vertices forming the edges
    V, *E = list(map(int, input.split()))
    # initialize a new graph
    G = Graph(V)
    # group the consequtice edge vertices and create edges on the graph
    for i in range(0, len(E), 2):
        G.addEdge(*E[i:i + 2])
    # create DAG of the input graph
    dag = G.DAG()
    # find the max nodes that could be traversed in the DAG
    dag.maxReachable()
