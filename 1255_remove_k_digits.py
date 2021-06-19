import heapq
class Solution_1:
    """
    @param num: a string
    @param k: an integer
    @return: return a string
    """
    def removeKdigits(self, num, k):
        # write your code here
        if not k:
            return num

        delete = 0
        digits = [int(c) for c in num]

        while delete < k:
            index = self.find_to_remove(digits)
            #print(index)
            digits = digits[:index] + digits[index+1:] if index < len(digits)-1 else digits[:index]
            delete += 1
        if not digits:
            return '0'
        return str(int(''.join([str(d) for d in digits])))

    def find_to_remove(self, digits):
        for i in range(len(digits) -1):
            if digits[i] > digits[i+1]:
                return i

        return len(digits)-1

class Solution:
    """
    @param num: a string
    @param k: an integer
    @return: return a string
    """
    def removeKdigits(self, num, k):
        if not k:
            return num

        if k >= len(num):
            return '0'

        stack = []
        for i, char in enumerate(num):
            while len(stack) > 0 and k > 0 and stack[-1] > char:
                stack.pop()
                k -= 1
            stack.append(char)
        print(stack)

        # the rest of number can be deleted from the tail
        ans = ''.join(stack[:len(stack)-k])

        # format the answer
        zero_i = 0
        for i in range(len(ans)):
            if ans[i] == '0':
                zero_i += 1
            else:
                break
        if zero_i == len(ans):
            return '0'
        return ans[zero_i:]
if __name__ == '__main__':
    s = Solution()
    num = "10200"
    k = 1
    print(s.removeKdigits(num, k))