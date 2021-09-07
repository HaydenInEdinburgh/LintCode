class Solution:
    """
    @param n: a Integer
    @return: the first n-line Yang Hui's triangle
    """
    def calcYangHuisTriangle(self, n):
        # write your code here
        if not n:
            return []

        triangle = []

        for i in range(n):
            sub = [0] * (i+1)
            sub[0], sub[-1] = 1, 1
            for j in range(1, i):
                sub[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(sub)

        return triangle

if __name__ == '__main__':
    s = Solution()
    n =2
    print(s.calcYangHuisTriangle(n))