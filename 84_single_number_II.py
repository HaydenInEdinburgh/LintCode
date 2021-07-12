class Solution:
    """
    @param A: An integer array
    @return: An integer array
    """
    def singleNumberIII(self, A):
        # write your code here
        if not A:
            return

        number = set()
        for n in A:
            if n not in number:
                number.add(n)
            else:
                number.remove(n)

        return list(number)