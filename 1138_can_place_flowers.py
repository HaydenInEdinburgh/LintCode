class Solution:
    """
    @param flowerbed: an array
    @param n: an Integer
    @return: if n new flowers can be planted in it without violating the no-adjacent-flowers rule
    """

    def canPlaceFlowers(self, flowerbed, n):
        # Write your code here
        if not n:
            return True
        if not flowerbed:
            return False

        possible_cnt = 0
        left, mid, right = None, None, flowerbed[0]
        for i in range(len(flowerbed)-1):
            left, mid, right = mid, right, flowerbed[i+1]
            if not (left or mid or right):
                mid = 1
                possible_cnt += 1

            if possible_cnt >= n:
                return True


        if not (mid or right):#the end two are empty
            possible_cnt += 1

        return possible_cnt >= n