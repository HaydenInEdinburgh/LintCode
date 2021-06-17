class Solution:
    """
    @param people: a random list of people
    @return: the queue that be reconstructed
    """
    def reconstructQueue(self, people):
        # write your code here
        if not people:
            return []

        sorted_ppl = sorted(people, key=lambda x: [-x[0], x[1]])
        print(sorted_ppl)
        res = []

        for height, index in sorted_ppl:
            res = res[:index] + [[height, index]] + res[index:]

        return res
if __name__ == '__main__':
    s = Solution()
    people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    s.reconstructQueue(people)