func findOrder(numCourses int, prerequisites [][]int) []int {
    graph := make(map[int][]int)
    in_degrees := make(map[int]int)
    
    for i := 0; i < numCourses; i++ {
        in_degrees[i] = 0
    }
    
    for _, prerequisite := range prerequisites {
        src, dst := prerequisite[1], prerequisite[0]
        graph[src] = append(graph[src], dst)
        in_degrees[dst] += 1
    }
    
    var queue []int
    for key := range in_degrees {
        if in_degrees[key] == 0 {
            queue = append(queue, key)
        }
    }
    
    var course_schedule []int
    
    for len(queue) > 0 {
        vertex := queue[0]
        queue = queue[1:]
        course_schedule = append(course_schedule, vertex)
        
        for _, neighbor := range graph[vertex] {
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0 {
                queue = append(queue, neighbor)
            }
        }
        
    }
    
    if len(course_schedule) != numCourses {
        return []int{}
    }
    
    return course_schedule
}
