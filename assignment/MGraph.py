
class MGraph:
    def __init__(self,n):
        self.graph = [[0] * n for _ in range(n)]  # values 0f matrix
        self.vertices = n # number of vertice
        self.visited = [0] * n # visited list to show a vertice is visited

    def set(self,v1, v2, value):  # set path v1 to v2
        self.graph[v1][v2] = value
        self.graph[v2][v1] = value

def reset_visited(G):
    G.visited = [0] * G.vertices

def BFS_all(G):
    result = []
    for i in range(G.vertices):
        if not G.visited[i]:
            result.extend(BFS(G, i))

    return result

def BFS(G, i):
    if not G.visited[i]:
        que = []
        que.append(i)
        G.visited[i] = 1
        path = []

        while que:
            v = que.pop(0)
            path.append(v)
            for j in range(G.vertices):
                if G.graph[v][j] and not G.visited[j]:
                    que.append(j)
                    G.visited[j] = 1  # when append j into que, set visited[j] = 1

        return path
    else:
        return []

if __name__ == "__main__":
    graph = MGraph(4)
    graph.set(0,1,1)
    graph.set(0,2,1)
    graph.set(1, 3, 1)
    graph.set(2, 3, 1)
    #print(graph.graph)
    path = BFS_all(graph)
    print(f"BFS path result {path}")
    print("BFS path result: ","-> ".join(map(str, path)))
