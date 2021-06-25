class Solution:
    """
    @param poured: an integer
    @param query_row: an integer
    @param query_glass: an integer
    @return: return a double
    """
    # Hint: Take care of numbers' structure
    def champagneTower(self, poured, query_row, query_glass):
        # write your code here
        res = [[0.0] * i for i in range(1, query_row + 2)]
        res[0][0] = poured

        for i in range(query_row):
            for j in range(len(res[i])):
                if res[i][j] <= 1:
                    continue
                res[i + 1][j] += (res[i][j] - 1.0) / 2.0
                res[i + 1][j + 1] += (res[i][j] - 1.0) / 2.0

        return float(res[query_row][query_glass]) if res[query_row][query_glass] < 1 else 1.0
