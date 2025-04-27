from collections import deque

def bfsForG(thread, src):

    #number of nodes
    num_nodes = len(thread)

    #visited path to output the path
    path = []

    #know if a node is visited 
    visited = [False] * num_nodes

    #create a deque
    q = deque()

    #start point
    q.append(src)

    while q:
        current = q.popleft()
        visited[current] = True
        path.append(current)

        for i in thread[current]:
            if visited[i] == False:
                visited[i] == True
                q.append(i)

    return path



if __name__ == "__main__":

    # create the adjacency list
    # [ [2, 3, 1], [0], [0, 4], [0], [2] ]
    adj = [[1], [0, 2, 3], [1], [1, 4], [3]]
    src = 0
    ans = bfsForG(adj, src)
    for i in ans:
        print(i, end=" ")
