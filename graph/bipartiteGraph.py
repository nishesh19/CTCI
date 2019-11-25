'''
Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.

Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.
'''


def isBipartite(graph):
    """
    :type graph: List[List[int]]
    :rtype: bool
    """
    colored = [None for i in range(len(graph))]
    visited = [False for i in range(len(graph))]

    while True:
        
        index = next((i[0] for i in enumerate(graph) if i[1] and not visited[i[0]]), None)
        if index is None:
            return True
        colored[index] = 0
        queue = [index]
        visited[index] = True
        while queue:
            curr = queue.pop(0)
            
            for node in graph[curr]:
                if node == curr:
                    # Self Loop
                    return False 
                if colored[node] is None:
                    colored[node] = colored[curr] ^ 1
                elif colored[node] == colored[curr]:
                    return False

                if not visited[index]:
                    queue.append(node)

    return True


if __name__ == '__main__':
    print(isBipartite([[2,4],[2,3,4],[0,1],[1],[0,1],[7],[9],[5],[],[6],[12,14],[],[10],[],[10],[19],[18],[],[16],[15],[23],[23],[],[20,21],[],[],[27],[26],[],[],[34],[33,34],[],[31],[30,31],[38,39],[37,38,39],[36],[35,36],[35,36],[43],[],[],[40],[],[49],[47,48,49],[46,48,49],[46,47,49],[45,46,47,48]]))
