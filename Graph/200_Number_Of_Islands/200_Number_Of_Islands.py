class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        seen = set()
        output = 0
        
        def dfs(row, col):                
            seen.add((row, col))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            
            for dr, dc in directions:
                new_dr = dr + row
                new_dc = dc + col
                if (new_dr in range(ROWS) and
                    new_dc in range(COLUMNS) and
                    grid[new_dr][new_dc] == "1" and
                    (new_dr, new_dc) not in seen):
                    dfs(new_dr, new_dc)
                
        
        for row in range(ROWS):
            for col in range(COLUMNS):
                if (row, col) not in seen and grid[row][col] == "1":
                    output += 1
                    dfs(row, col)
                    
        return output
