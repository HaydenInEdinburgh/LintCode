class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        if len(numbers) < 3: return

        numbers = sorted(numbers)
        res = None

        for i in range(len(numbers)):
            left, right = i+1, len(numbers)-1
            while left < right:
                cur_sum = numbers[i] + numbers[left] + numbers[right]
                if res is None or abs(cur_sum - target) < abs(res - target):
                    res = cur_sum
                if cur_sum > target:
                    right -= 1
                else:
                    left += 1

        return res
