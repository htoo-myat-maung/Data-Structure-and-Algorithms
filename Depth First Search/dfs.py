def dfs(adj, src):
    path = []
    visited = [False] * len(adj)

    dfs_return(adj, visited, src, path)

    return path

def dfs_return(adj, visited, s, p):
    p.append(s)
    visited[s] = True

    for a in adj[s]:
        if visited[a] == False:
            dfs_return(adj, visited, a, p)


def switch(adj, a,b):
    adj[a].append(b)
    adj[b].append(a)

if __name__ == "__main__":
    V = 5

    # Create an adjacency list for the graph
    adj = [[] for _ in range(V)]

    # Define the edges of the graph
    edges = [[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]]

    # Populate the adjacency list with edges
    for e in edges:
        switch(adj, e[0], e[1])
        print(adj)
    

    source = 1
    print("DFS from source:", source)
    a = dfs(adj, source)
    print(a)
