import collections


class Solution:
    """
    @param numCourses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """

    def canFinish(self, numCourses, prerequisites):
        # write your code here
        if not numCourses or not prerequisites:
            return True
        in_degrees, pre_to_later = self.get_indegree(numCourses, prerequisites)
        start_courses = [x for x, v in in_degrees.items() if v == 0]
        cnt = len(start_courses)
        queue = collections.deque(start_courses)

        while queue:
            node = queue.popleft()
            for later in pre_to_later[node]:
                in_degrees[later] -= 1
                if in_degrees[later] == 0:
                    queue.append(later)
                    cnt += 1
        return cnt == numCourses

    def get_indegree(self, numCourses, prerequisites):
        indegrees = {x: 0 for x in range(numCourses)}
        pre_to_later = {x: [] for x in range(numCourses)}
        for later, pre in prerequisites:
            indegrees[later] += 1
            pre_to_later[pre].append(later)
        return indegrees, pre_to_later
