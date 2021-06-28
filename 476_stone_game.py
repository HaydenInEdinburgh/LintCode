class Solution:
    def stoneGame(self, piles) -> bool:
        if not piles: return

        self.dp = {}
        N = len(piles)
        self.choose_max_gap(piles, 0, N - 1)
        print(self.dp)
        return self.dp[(0, N-1)] > 0

    def choose_max_gap(self, piles, left, right):
        if left == right:
            #there's only one pile left
            return piles[left]

        if (left, right) in self.dp:
            return self.dp[(left, right)]

        choose_left = piles[left] - self.choose_max_gap(piles, left +1, right)
        choose_right = piles[right] - self.choose_max_gap(piles, left, right-1)
        self.dp[(left, right)] = max(choose_left, choose_right)

        return self.dp[(left, right)]

if __name__ == '__main__':
    s = Solution()
    piles = [5, 3, 4, 5]
    print(s.stoneGame(piles))