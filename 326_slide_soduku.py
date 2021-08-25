class Solution:
    """
    @param number: an only contains from 1 to 9 array
    @return: return  whether or not each sliding window position contains all the numbers for 1 to 9
    """
    def SlidingWindows(self, number):
        # write your code here
        n = len(number[0])
        if not n:
            return []

        dig_set = {}
        res = []
        #move
        l, r = 0, 2
        while r < n:
            # init
            if r == 2:
                for i in range(3):
                    for j in range(3):
                        num = number[i][j]
                        dig_set[num] = dig_set.get(num, 0) + 1
            else:
                for i in range(3):
                    num_l = number[i][l]
                    dig_set[num_l] -= 1
                    if dig_set[num_l] == 0:
                        del dig_set[num_l]

                    num_r = number[i][r]
                    dig_set[num_r] = dig_set.get(num_r, 0)+1
                l += 1
            r += 1
            res.append(len(dig_set) == 9)


        return res

if __name__ == '__main__':
    s = Solution()
    numbers = [[1,2,3,2,5,7],[4,5,6,1,7,6],[7,8,9,4,8,3]]
    print(s.SlidingWindows(numbers))