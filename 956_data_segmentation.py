class Solution:
    """
    @param str: The input string
    @return: The answer
    """
    def dataSegmentation(self, string):
        # Write your code here
        if not string:
            return []

        res = []
        word = ''

        for char in string:
            if char.isalnum():
                word += char
            else:
                if word:
                    res.append(word)
                    word = ''
                if char != ' ':
                    res.append(char)

        if word:
            res.append(word)

        return res

if __name__ == '__main__':
    s = Solution()
    string = "(hi (i am)bye)"
    print(s.dataSegmentation(string))