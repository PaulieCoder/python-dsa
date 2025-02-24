class Graph:

    def __init__(self):
        self.graph = {}
    
    def insert(self, edges_list):
        """
        PARAMETERS
        edges_list - List[List[int]]
        return type - boolean
        """
        # forming the graph representation adjacency list
        # Time - O(n)
        try:
            for edge in edges_list:
                vertex = edge[0]
                if vertex in self.graph:
                    self.graph[vertex].append(edge[1])
                else:
                    self.graph[vertex] = [edge[1]]
            return True
        except IndexError as ex:
            return False
    
    def doDFS(self):
        visited = set()
        path = []
        # DFS for each vertex
        def dfs_helper(vertex):
            visited.add(vertex)
            path.append(vertex)
            for neighbour in self.graph[vertex]:
                # cycle found
                if neighbour in visited:
                    pass
                # other_vertex doesnt have any other neighbours
                elif neighbour not in self.graph.keys():
                    visited.add(neighbour)
                    path.append(neighbour)
                else:
                    dfs_helper(neighbour)
            return path
        
        for vertex in self.graph.keys():
            path = dfs_helper(vertex)
            print("DFS for vertex {} \n{}".format(vertex, path))
            visited.clear()
            path.clear()
    
if __name__ == "__main__":
    edges_list = [[1,2],[1,3],[2,4],[3,4],[3,5],[5,6]]
    graph = Graph()
    graph.insert(edges_list)
    graph.doDFS()