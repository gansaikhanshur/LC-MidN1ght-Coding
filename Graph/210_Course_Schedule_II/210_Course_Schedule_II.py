class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        in_degrees = {i: 0 for i in range(numCourses)}
        
        for prerequisite in prerequisites:
            src, dst = prerequisite[0], prerequisite[1]
            graph[src].append(dst)
            in_degrees[dst] += 1
            
        sources = collections.deque()
        
        for key in in_degrees:
            if in_degrees[key] == 0:
                sources.append(key)

        course_ordering = []
        while sources:
            vertex = sources.popleft()
            course_ordering.insert(0, vertex)
            
            for child in graph[vertex]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    sources.append(child)
                    
        if len(course_ordering) != numCourses:
            return []
        
        return course_ordering
