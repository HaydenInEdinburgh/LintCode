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
        # write your code here
        if not digits:
            return []

        res = []
        self.dfs(digits, res, [], 0)

        return res

    def dfs(self, digits, res, path, idx):
        if idx == len(digits):
            res.append(''.join(path))
            return

        for i in range(len(KEYBOARD[digits[idx]])):
            letter = KEYBOARD[digits[idx]][i]
            path.append(letter)
            self.dfs(digits, res, path, idx+1)
            path.pop()


if __name__ == '__main__':
    input = "22"
    expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    s = Solution()
    output = s.letterCombinations(input)
    print(output)