class Solution:
    """
    @param S: a string
    @return: a list of integers representing the size of these parts
    """
    def partitionLabels(self, S):
        # Write your code here
        if not S:
            return []

        #get start and end of the char in S
        char_to_start_end = {}
        for i, char in enumerate(list(S)):
            if char not in char_to_start_end:
                char_to_start_end[char] = [i, i]
            else:
                char_to_start_end[char][1] = i

        start, end = 0, 0
        res = []
        for v in sorted(char_to_start_end.values()):
            cur_start, cur_end = v
            if cur_start > end:
                res.append(end - start + 1)
                start, end = cur_start, cur_end
                continue

            if cur_start>=start and cur_end > end:
                end = cur_end
                continue

        res.append(end-start+1)
        return res

if __name__ == '__main__':
    solution = Solution()
    S = "abcab"
    print(solution.partitionLabels(S))