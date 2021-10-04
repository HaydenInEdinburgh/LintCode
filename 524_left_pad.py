class StringUtils:
    """
    @param: originalStr: the string we want to append to
    @param: size: the target length of the string
    @param: padChar: the character to pad to the left side of the string
    @return: A string
    """
    @classmethod
    def leftPad(self, originalStr, size, padChar=' '):
        # write your code here
        n = len(originalStr)
        if n >= size:
            return originalStr

        lack_num = size -n
        add_string = ''
        for _ in range(lack_num):
            add_string += padChar

        return add_string + originalStr