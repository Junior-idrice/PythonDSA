

num_nodes  = 5

edges = [(0,1),(0,4),(1,4),(1,3),(1,2),(3,4),(3,2)]

class Graph:
    def __init__(self,num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]

        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
    def matrix(self,num_nodes, edges):
        matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
        for i in range(num_nodes):
            for j in range(num_nodes):
                if (i, j) in edges or (j, i) in edges:
                    matrix[i][j] = 1
        for i,j in enumerate(matrix):
            print(i,j)


    def __repr__(self):
        # as an adjacency list
        return "\n".join(["{}: {}".format(n, neighbours) for n, neighbours in enumerate(self.data)])
    def __str__(self):
        return self.__repr__()



graph1= Graph(num_nodes, edges)
#print(graph1)
#graph1.matrix(num_nodes, edges)

# Graph traversal BFS

def bfs(graph, root):
    queue = []

    distance = [None] * len(graph.data)
    parent = [None]* len(graph.data)

    discoverd = [False]*len(graph.data)
    discoverd[root] = True
    distance[root] = 0
    queue.append(root)
    idx = 0

    while idx< len(queue):
        #deque
        current = queue[idx]
        idx += 1 

        #check all the edges

        for node in graph.data[current]:
            if not discoverd[node]:
                distance[node] = 1 + distance[current]
                parent[node] = current
                discoverd[node] = True
                queue.append(node)

    return queue, distance, parent

#print(bfs(graph1, 3))


# implementation of DFS

def dfs(graph, root):
    stack = []
    discovered = [False] * len(graph.data)
    result = []

    stack.append(root)

    while len(stack)> 0:
        current = stack.pop()
        if not discovered[current]:
            discovered[current] =True
            result.append(current)
            for node in graph.data[current]:
                if not discovered[node]:
                  stack.append(node)

    return result

#print(dfs(graph1, 3))
     
# My bfs

from collections import deque
def mybfs(graph, root):
    queue = deque([root])
    visited = [root]

    while queue:
        current = queue.popleft()
        print(current)

        for i in graph.data[current]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
#print(mybfs(graph1, 0))


# Weighted graphs 
num_nodes1 = 9
egdes1 = [(0,1,3),(0,3,2),(0,8,4),(1,7,4),(2,7,2),(2,3,6),(2,5,1),
          (3,4,1),(4,8,8),(5,6,8)]
#print(len(egdes1))
#Direct grap
num_nodes2 = 5
edges2 = [(0,1),(1,2),(2,3),(2,4),(4,2),(3,0)]


#class for all the type of graphs, direct, weighted and undirected graph

class Bgraph:
    def __init__(self, num_nodes, edges,directed=False, weighted = False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = weighted
        self.data = [[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]

        for edge in edges:
            if self.weighted:
                node1,node2,weight = edge
                self.data[node1].append(node2)
                self.weight[node1].append(weight)
                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(weight)
            else:
                 node1,node2= edge
                 self.data[node1].append(node2)
                 if not directed:
                     self.data[node2].append(node1)

    def __repr__(self):
        result = ""
        if self.weighted:
            for i, (nodes, weights) in enumerate(zip(self.data, self.weight)):
                result += "{}:{}\n".format(i, list(zip(nodes, weights)))
        else:
            for i, nodes in enumerate(self.data):
                result += "{}:{}\n".format(i, nodes)    
        return result
    def __str__(self):
        return self.__repr__()

num_nodes1 = 9
egdes1 = [(0,1,3),(0,3,2),(0,8,4),(1,7,4),(2,7,2),(2,3,6),(2,5,1),
          (3,4,1),(4,8,8),(5,6,8)]
#print(len(egdes1))
#Direct grap
num_nodes2 = 5
edges2 = [(0,1),(1,2),(2,3),(2,4),(4,2),(3,0)]
                     
num_nodes  = 5

edges = [(0,1),(0,4),(1,4),(1,3),(1,2),(3,4),(3,2)]
gra1 = Bgraph(num_nodes2, edges2, weighted=False, directed=True)
#print(len(gra1.data))


#SHORTEST PATH
#DIJKSTRA'S 

number_node3 = 6
edges3 = [(0,1,4),(0,2,2),(1,2,5),(1,3,10),(2,4,3),(4,3,4),(3,5,11)]

def shortest_path(graph,source, target):
    visited = [False]*len(graph.data)
    parent = [None]*len(graph.data)
    distance = [float('inf')]* len(graph.data)
    queue = []


    distance[source] = 0
    queue.append(source)
    idx = 0
    while idx< len(queue) and not visited[target]:
        current = queue[idx]
        visited[current] = True
        idx +=1
        #updata the distance of all its neighbors
        update_distance(graph, current, distance,parent)

        #find the first unvisited node with the smallest distance
        next_node = pick_next_node(distance, visited)
        if next_node:
            queue.append(next_node)

        visited[current] = True
    return distance[target], parent

def update_distance(graph,current,distance, parent= None):
    neighbors = graph.data[current]
    weights= graph.weight[current]
    for i,node in enumerate(neighbors):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current]  + weight
            if parent:
                parent[node] = current

def pick_next_node(distance,visited):
    min_distance = float('inf')
    min_node = None

    for node in range(len(distance)):
        if not visited[node] and distance[node]< min_distance:
            min_node = node
            min_distance = distance[node]
    return min_node

number_node3 = 6
edges3 = [(0,1,4),(0,2,2),(1,2,5),(1,3,10),(2,4,3),(4,3,4),(3,5,11)]

graph10 = Bgraph(number_node3, edges3, weighted=True, directed=True)
print(graph10)

print(shortest_path(graph10, 0, 5))