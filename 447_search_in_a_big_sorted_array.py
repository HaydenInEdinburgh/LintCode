class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        if not reader:
            return -1

        r = 2
        end = reader.get(r)
        while end < target:
            r *= 2
            end = reader.get(r)

        l=0
        while l+1 < r:
            mid = (l +r)//2
            if reader.get(mid) < target:
                l = mid
            else:
                r = mid

        if reader.get(l) == target:
            return l
        if reader.get(r) == target:
            return r
        return -1