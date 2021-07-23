"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    """
    @param coordinates: The radars' coordinate
    @param radius: Detection radius of radars
    @return: The car was detected or not
    """
    def radarDetection(self, coordinates, radius):
        # Write your code here
        if not coordinates:
            return 'YES'

        for i, point in enumerate(coordinates):
            l = point.y - radius[i]
            r = point.y + radius[i]
            if (l < 0 and r > 0) or (l<1 and r>1):
                return 'YES'

        return 'NO'