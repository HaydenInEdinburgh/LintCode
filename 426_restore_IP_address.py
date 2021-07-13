class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
    """
    invalid address
    start with 0
    more than 3 dot
    bigger than 255
    """
    def restoreIpAddresses(self, s):
        # write your code here
        if not s:
            return []
        res = []
        self.dfs(s, 0, 0, "", res)
        return res

    def dfs(self, s, idx, dot, path, res):
        if dot > 3:
            return
        # idx comes to the end
        if idx == len(s):
            if dot == 3:
                nums = path.split('.')
                for n in nums:
                    if len(n) > 3 and n.startswith('0'):
                        return
                    if int(n) > 255:
                        return
                res.append(path)
                return
            return
        # not add dot
        self.dfs(s, idx+1, dot, path+s[idx], res)
        # add dot
        if idx < len(s)-1:
            self.dfs(s, idx+1, dot+1, path+s[idx]+'.', res)

if __name__ == '__main__':
    s = Solution()
    string = "25525511135"
    print(s.restoreIpAddresses(string))