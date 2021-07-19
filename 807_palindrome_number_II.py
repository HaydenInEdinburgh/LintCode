class Solution:
    """
    @param n: non-negative integer n.
    @return: return whether a binary representation of a non-negative integer n is a palindrome.
    """
    def isPalindrome(self, n):
        # Write your code here

        bin_n = bin(n).replace("0b", "")

        return bin_n == bin_n[::-1]
if __name__ == '__main__':
    print(bin(4).replace("0b", ""))