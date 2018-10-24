class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = ''
        n = num
        while n > 0:
            if n & 1 == 1:
                result += '0'
            else:
                result += '1'
            n >>= 1
        return int(result[::-1], 2)






        """
        Given a positive integer, output its complement number. The complement strategy is to flip the bits
        of its binary representation.

        Note:
        The given integer is guaranteed to fit within the range of a 32-bit signed integer.
        You could assume no leading zero bit in the integer’s binary representation.
        Example 1:
        Input: 5
        Output: 2
        Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010.
        So you need to output 2.
        """
