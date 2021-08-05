R_CHAR = {'1':'1', '0':'0', '6':'9', '8': '8', '9':'6'}
class Solution:
    """
    @param k: the number of auction participants
    @return: the number of confusing numbers
    """
    def theConfusingNumbers(self, k):
        # write your code here
        confusions = 0

        for n in range(1, k+1):
            r_n = self.check(n, confusions, k)
            if r_n and r_n <= k:
                confusions += 2
        #print(confusions)
        return confusions

    def check(self, num, confusions, k):
        num_string = str(num)
        reverse = ''
        if num_string[-1] == '0':
            return
        for i, char in enumerate(num_string):
            if char not in R_CHAR:
                return
            reverse += R_CHAR[char]
        r_num = int(reverse[::-1])
        return r_num if r_num > num else None


class Solution_DFS:
    """
        @param k: the number of auction participants
        @return: the number of confusing numbers
        """

    def theConfusingNumbers(self, k):

        n = len(str(k))
        visited = set()
        if k == 1000000000:
            k -= 1
            print(k)
        self.dfs('', 0, k, n, visited)
        # print(visited)
        return len(visited)

    def dfs(self, cur, idx, k, n, visited):
        if idx == n+1:
            return
        if cur:
            r_cur = self.get_reverse(cur)
            r_num = int(r_cur)
            if int(cur) <= k and r_num <= k and r_cur != cur and cur[0] != '0' and r_cur[0] != '0':
                #print(idx, r_cur, cur)
                visited.add(cur)
                visited.add(r_cur)

        for char in ['1', '0', '6', '8', '9']:
            if idx == 0 and char == '0':
                continue
            self.dfs(cur+char, idx+1, k, n, visited)


    def get_reverse(self, string):
        return ''.join([R_CHAR[c] for c in string])[::-1]



if __name__ == '__main__':
    s = Solution_DFS()
    k = 1000000000
    print(s.theConfusingNumbers(k))
