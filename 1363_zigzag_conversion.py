class Solution:
    """
    @param s: the given string
    @param numRows: the number of rows
    @return: the string read line by line
    """
    def convert(self, s, numRows):
        # Write your code here
        if not s or numRows < 2:
            return s

        res_array = [[] for _ in range(numRows)]
        for i, char in enumerate(s):
            row_idx = self.get_idx(i, numRows)
            res_array[row_idx].append(char)

        return self.str_format(res_array)

    def get_idx(self, i, numRows):
        size = 2*numRows - 2
        row_idx = i % size if i % size < numRows else (numRows - 1) - (i % (numRows - 1))
        return row_idx

    def str_format(self, arr):
        return ''.join([''.join(subarr) for subarr in arr])

if __name__ == '__main__':
    s = Solution()
    input = "PAYPALISHIRING"
    n = 1
    print(s.convert(input, n))