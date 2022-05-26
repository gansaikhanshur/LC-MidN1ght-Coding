class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {i: [] for i in range(numCourses)}
        in_degrees = {i: 0 for i in range(numCourses)}
        
        for prerequisite in prerequisites:
            course_to_take = prerequisite[0]
            course_prereq = prerequisite[1]
            graph[course_to_take].append(course_prereq)
            in_degrees[course_prereq] += 1
            
        sources = collections.deque()
        for key in in_degrees:
            if in_degrees[key] == 0:
                sources.append(key)
                
        course_schedules = []
        while sources:
            vertex = sources.popleft()
            course_schedules.append(vertex)
            for neighbor in graph[vertex]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    sources.append(neighbor)
                    
        return len(course_schedules) == numCourses
