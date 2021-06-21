import collections

#BFS
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        if not prerequisites or not  numCourses:
            return
        indegrees, nextCourse = self.get_indegrees(numCourses, prerequisites)
        start_courses = [x for x in indegrees.keys() if indegrees[x] == 0]
        queue = collections.deque(start_courses)

        res = start_courses[:]
        visited = set(start_courses)
        while queue:
            cur = queue.popleft()
            for next in nextCourse[cur]:
                if next in visited:
                    continue
                indegrees[next] -= 1
                if indegrees[next] == 0:
                    queue.append(next)
                    visited.add(next)
                    res.append(next)

        if len(res) == numCourses:
            return res
        return []

    def get_indegrees(self, numCourses, prerequisites):
        indegrees = {x: 0 for x in range(numCourses)}
        nextCourse = {x: [] for x in range(numCourses)}
        for next, pre in prerequisites:
            indegrees[next] = indegrees[next] + 1
            nextCourse[pre].append(next)
        return indegrees, nextCourse