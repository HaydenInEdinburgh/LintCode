class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, nums):
        # write your code here
        if len(nums) <= 1:
            return [1]

        front_product = []
        back_product = []

        tmp = 1
        for i in range(len(nums)):
            tmp *= nums[i]
            front_product.append(tmp)
        tmp = 1
        for j in range(len(nums)-1, -1, -1):
            tmp *= nums[j]
            back_product.append(tmp)
        back_product = back_product[::-1]

        res = []
        for i in range(len(nums)):
            if i == 0:
                product = back_product[1]
            elif i == len(nums)-1:
                product = front_product[-2]
            else:
                product = front_product[i-1] * back_product[i+1]
            res.append(product)

        return res

if __name__ == '__main__':
    s = Solution()
    nums = [2,4,6]
    print(s.productExcludeItself(nums))