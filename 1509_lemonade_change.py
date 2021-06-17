class Solution:
    """
    @param bills: the Bill
    @return: Return true if and only if you can provide every customer with correct change.
    """
    def lemonadeChange(self, bills):
        # Write your code here.

        changes = {5: 0, 10: 0}

        for bill in bills:
            if bill == 5:
                changes[5] += 1
            if bill == 10:
                if changes[5] < 1:
                    return False
                changes[5] -= 1
                changes[10] += 1
            if bill == 20:
                if changes[10] >= 1 and changes[5] >= 1:
                    changes[10] -= 1
                    changes[5] -= 1
                elif changes[5] >= 3:
                    changes[5] -= 3
                else:
                    return False

        return True

if __name__ == '__main__':
    s = Solution()
    bills = [5,5,5,10,20]
    print(s.lemonadeChange(bills))