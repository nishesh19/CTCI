import math
class Solution:
    def wallsAndGates(self, rooms) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        self.inf = 2**31-1 
        distances = {}
        for i in range(len(rooms)):
            
            for j in range(len(rooms[0])):
                if rooms[i][j] == self.inf:
                    rooms[i][j] = self.dfs(rooms,i,j,distances,set())
    
    def dfs(self,rooms,i,j,distances,visited):
        if (i,j) in distances and distances[(i,j)] != self.inf:
            return distances[(i,j)]

        if rooms[i][j] == 0:
            return 0

        if rooms[i][j] == -1:
            return self.inf

        visited.add((i,j))
        neighbors = [[-1,0],[0,1],[1,0],[0,-1]]
        min_distance = self.inf
        for r,c in neighbors:
            if 0 <= i+r < len(rooms) and 0 <= j+c < len(rooms[0]) and ((i+r,j+c) not in visited):
                min_distance = min(min_distance,self.dfs(rooms,i+r,j+c,distances,visited))

        distances[(i,j)] = min_distance if min_distance == self.inf else 1 + min_distance
        return distances[(i,j)]
        
rooms = [[0,2147483647,2147483647,0,-1,-1,0,0,0,-1,-1,0,2147483647,2147483647],[2147483647,-1,2147483647,-1,2147483647,0,-1,2147483647,-1,2147483647,2147483647,-1,-1,2147483647],[0,0,-1,2147483647,-1,2147483647,-1,-1,2147483647,0,0,2147483647,0,2147483647],[-1,0,2147483647,-1,0,0,-1,2147483647,0,2147483647,0,-1,0,-1]]

Solution().wallsAndGates(rooms)
print(rooms)

        
        