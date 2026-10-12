class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            temp = i
            count = 0
            while temp:
                if (temp & 0x1) == 0x1:
                    count += 1
                temp >>= 1
            output.append(count)
        return output