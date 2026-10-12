class Solution:

    from collections import Counter

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        cnt_s, cnt_t = Counter(s), Counter(t)

        return cnt_s == cnt_t