class Solution:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    """
    def productExceptSelf(self, nums):
        # write your code here
        if not nums:
            return None

        zero_cnt = 0
        product = 1
        for n in nums:
            if not n:
                zero_cnt += 1
                continue
            product *= n

        res = []
        for n in nums:
            if n == 0:
                if zero_cnt > 1:
                    res.append(0)
                else:
                    res.append(product)
            else:
                if zero_cnt >= 1:
                    res.append(0)
                else:
                    res.append(product//n) # product/n is a float type number

        return res

