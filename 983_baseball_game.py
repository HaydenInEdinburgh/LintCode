class Solution:
    """
    @param ops: the list of operations
    @return:  the sum of the points you could get in all the rounds
    """
    def calPoints(self, ops):
        # Write your code here
        if not ops:
            return 0

        valid = []
        for i, char in enumerate(ops):
            print(valid)
            if char.isdigit():
                valid.append(int(char))
            elif len(char) > 1:
                valid.append(-1 * int(char[1:]))
            if char == "C":
                valid.pop()
            if char == "+":
                #print(valid[-2:])
                valid.append(sum(valid[-2:]))
            if char == "D":
                valid.append(2 * valid[-1])
        #print(valid)
        return sum(valid)

if __name__ == '__main__':
    s = Solution()
    ops = ["61","-50","65","+","D","-99","-58","88","19","-11"]
    print(s.calPoints(ops))