class Graph_Vertex:
    def __init__(self, label:str) -> None:
        self.label = label
        self.edges= [] # First create with empty edges.
    def __str__(self):
        msg = f'{self.label}:'
        for i in self.edges:
            msg += f"{self.label}-->{i.label};"
        return msg 

class BFS_Graph(Graph_Vertex):
    def __init__(self, label: str) -> None:
        super().__init__(label)
        self.distance = -1
        self.parent = None
def bfs(start: Graph_Vertex):
    # start from specific vertex and traverse
    queue = []
    start.distance = 0
    queue.append(start)
    while queue:
        current_vertex = queue.pop()
        process_vertex_early(current_vertex.label)
        for edge in current_vertex.edges:
            if edge.distance == -1:
                process_edge(current_vertex.label,edge.label)
                edge.distance = current_vertex.distance + 1
                edge.parent = current_vertex.label
                queue.append(edge)
        process_vertex_late(current_vertex.label)
    print("Over !!")

def initial_graph(n: int, edges_list:list) -> None:
    # Initial general graph
    graphs=[]
    for i in range(n):
        graphs.append(Graph_Vertex(i))
    for edge in edges_list:
        if 0<= edge[0] < n and 0 <= edge[1] < n:
            graphs[edge[0]].edges.append(graphs[edge[1]])
    return graphs

def bfs_initial_graph(n: int, edges_list:list) -> None:
    # Initial graph object for BFS operation
    graphs=[]
    for i in range(n):
        graphs.append(BFS_Graph(i))
    for edge in edges_list:
        if 0<= edge[0] < n and 0 <= edge[1] < n:
            graphs[edge[0]].edges.append(graphs[edge[1]])
    return graphs

def process_vertex_early(label:int):
    print("Processing vertex",label)

def process_edge(i:int, j:int):
    print(f"Processing edge ({i}, {j})")

def process_vertex_late(label:int):
    print(f"Vertex {label} processed")

if __name__ == "__main__":
    # General graph example
    edges_list=[[2,4],[4,2],[1,4],[4,1],[3,4],[4,3],[1,3],[3,1]]
    graphs = initial_graph(5, edges_list)
    for vertex in graphs:
        print(vertex)
    print("---------------")


    # BFS example
    edge_list=[[1,2],[2,1],[1,5],[5,1],[1,6],[6,1],[2,3],[3,2],[2,5],[5,2],[3,4],[4,3],[4,5],[5,4]]
    graph_bfs = bfs_initial_graph(7, edge_list)
    bfs(graph_bfs[1])
    for v in graph_bfs:
        print(v)

