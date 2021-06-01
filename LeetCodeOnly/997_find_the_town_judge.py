class Solution:
    def findJudge(self, n, trust) -> int:
        if not n:
            return -1

        in_degrees, out_degrees = self.get_indegree(n, trust)
        for i in range(1, n+1):
            if in_degrees[i] == 0 and out_degrees[i] == n-1:
                return i

        return -1


    def get_indegree(self, n, trust):
        in_degrees = {x: 0 for x in range(1, n+1)}
        out_degrees = {x: 0 for x in range(1, n+1)}
        for a, b in trust:
            #a trust b
            in_degrees[a] += 1
            out_degrees[b] += 1

        return in_degrees, out_degrees