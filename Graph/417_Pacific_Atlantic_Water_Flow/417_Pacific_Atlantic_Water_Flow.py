# https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, columns = len(heights), len(heights[0])
        can_reach_pacific = set()
        can_reach_atlantic = set()
        
        def dfs(row, col, visited_cell, prev_cell):
            if (row not in range(rows) or
                col not in range(columns) or
                (row, col) in visited_cell or
                heights[row][col] < prev_cell):
                return
            visited_cell.add((row, col))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                new_dr = dr + row
                new_dc = dc + col
                dfs(new_dr, new_dc, visited_cell, heights[row][col])
        
        for row in range(rows):
            dfs(row, 0, can_reach_pacific, heights[row][0])
            dfs(row, columns - 1, can_reach_atlantic, heights[row][columns - 1])
            
        for column in range(columns):
            dfs(0, column, can_reach_pacific, heights[0][column])
            dfs(rows - 1, column, can_reach_atlantic, heights[rows - 1][column])
            
        return can_reach_pacific.intersection(can_reach_atlantic)
