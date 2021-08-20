class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here
        if not nums1 or not nums2:
            return []
        p1, p2 = 0, 0
        intersection = []
        nums1.sort()
        nums2.sort()

        while p1< len(nums1) and p2< len(nums2):
            n1, n2 = nums1[p1], nums2[p2]
            if n1 < n2:
                p1 += 1
                while p1< len(nums1) and nums1[p1] == nums1[p1-1]:
                    p1 += 1
            elif n1 > n2:
                p2 += 1
                while p2< len(nums2) and nums2[p2] == nums2[p2-1]:
                    p2 += 1
            else:
                if n1 not in intersection:
                    intersection.append(n1)
                p1 += 1
                p2 += 1

        return intersection

if __name__ == '__main__':
    s = Solution()
    a = [1, 2, 2, 1]
    b = [2, 2]
    print(s.intersection(a,b))