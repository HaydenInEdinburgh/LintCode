class Solution:
    def reorderLogFiles(self, logs):
        if not logs:
            return []

        codes = {x: self.get_code(x, index) for index, x in enumerate(logs)}

        return sorted(logs, key=lambda x: codes[x])

    def get_code(self, string, index):
        tokens = string.split(' ')
        isdigit = tokens[-1].isdigit()
        words = index if isdigit else ' '.join(tokens[1:])
        code = tokens[0]
        return (isdigit, words, code)


if __name__ == '__main__':
    s = Solution()
    logs = ["j mo", "5 m w", "g 07", "o 2 0", "t q h"]
    print(s.reorderLogFiles(logs))