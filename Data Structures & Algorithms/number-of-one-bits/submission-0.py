class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if (n & 0x1) == 0x1:
                count += 1
            n >>= 1
        return count
