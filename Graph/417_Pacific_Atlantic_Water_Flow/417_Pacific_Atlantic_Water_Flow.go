func pacificAtlantic(heights [][]int) [][]int {
    rows, columns := len(heights), len(heights[0])
    can_reach_pacific := makeArray(rows, columns)
    can_reach_atlantic := makeArray(rows, columns)
    var result [][]int
    
    for r := 0; r < rows; r++ {
        dfs(r, 0, heights, can_reach_pacific, heights[r][0])
        dfs(r, columns - 1, heights, can_reach_atlantic, heights[r][columns - 1])
    }
    
    for c := 0; c < columns; c++ {
        dfs(0, c, heights, can_reach_pacific, heights[0][c])
        dfs(rows - 1, c, heights, can_reach_atlantic, heights[rows - 1][c])
    }
    
    for r := range heights {
        for c := range heights[0] {
            if can_reach_pacific[r][c] && can_reach_atlantic[r][c] {
                result = append(result, []int{r, c})
            }
        }
    }
    
    return result
    
}

func dfs(row int, col int, matrix [][]int, visited_cells [][]bool, prev_cell int){
    rows, columns := len(matrix), len(matrix[0])
    if row < 0 || row >= rows || col < 0 || col >= columns || visited_cells[row][col] || matrix[row][col] < prev_cell {
        return
    }
    visited_cells[row][col] = true
    
    directions := [][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
    for _, direction := range directions{
        new_dr := direction[0] + row
        new_dc := direction[1] + col
        dfs(new_dr, new_dc, matrix, visited_cells, matrix[row][col])
    }
    
}

func makeArray(row int, col int) [][]bool {
    output := make([][]bool, row)
    
    for idx := range output{
        output[idx] = make([]bool, col)
    }
    
    return output
}
