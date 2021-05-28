KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        if not digits:
            return []

        res = []
        self.dfs(digits, 0, res, [])
        return res

    def dfs(self, digits, index, res, path):
        if len(path) == len(digits):
            res.append(''.join(path))
            return

        for char in KEYBOARD[digits[index]]:
            path.append(char)
            self.dfs(digits, index+1, res, path)
            path.pop()


if __name__ == '__main__':
    input = '22'
    s = Solution()
    print(s.letterCombinations(input))