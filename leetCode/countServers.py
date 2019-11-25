class Solution:
    def countServers(self, grid) -> int:
        total_count = 0
        rows = len(grid)
        columns = len(grid[0])
        
        row_count = [0 for _ in range(rows)]
        column_count = [0 for _ in range(columns)]
        
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]:
                    row_count[i] += 1
                    column_count[j] += 1
        
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] and ((row_count[i] > 1) or (column_count[j] > 1)):
                    total_count += 1
        
        return total_count
                    
                        
if __name__ == '__main__':
    sol = Solution()
    
    grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
    print(sol.countServers(grid))                        
                        
                    
                
                                            
        