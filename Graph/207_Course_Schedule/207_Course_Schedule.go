func canFinish(numCourses int, prerequisites [][]int) bool {
    graph := make(map[int][]int)
    in_degree := make(map[int]int)
    
    for i := 0; i < numCourses; i++ {
        in_degree[i] = 0
    }
    
    for _, prerequisite := range prerequisites{
        src, dst := prerequisite[0], prerequisite[1]
        graph[src] = append(graph[src], dst)
        in_degree[dst] += 1
    }

    var queue []int
    for key := range in_degree{
        if in_degree[key] == 0 {
            queue = append(queue, key)
        }
    }

    var course_schedules []int
    for len(queue) > 0 {
        vertex := queue[0]
        queue = queue[1:]
        course_schedules = append(course_schedules, vertex)
        
        for _, child := range graph[vertex] {
            in_degree[child] -= 1
            if in_degree[child] == 0 {
                queue = append(queue, child)
            }
        }
        
    }

    return len(course_schedules) == numCourses
    
}
