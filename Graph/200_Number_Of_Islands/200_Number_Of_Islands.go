func numIslands(grid [][]byte) int {
    output := 0
    
    for i, row := range grid {
        for j, _ := range row {
            if grid[i][j] == '1' {
                visit(grid, i, j)
                output += 1
            }
        }
    }
    
    return output
}

func visit(grid [][]byte, row int, col int) {
    ROWS, COLUMNS := len(grid), len(grid[0])
    
    if (row < 0 || row >= ROWS || col < 0 || col >= COLUMNS || grid[row][col] == '0') {
        return
    }
    
    grid[row][col] = '0'
    
    directions := [][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
    
    for _, direction := range directions {
        new_dr := direction[0] + row
        new_dc := direction[1] + col

        visit(grid, new_dr, new_dc)
    }
}
