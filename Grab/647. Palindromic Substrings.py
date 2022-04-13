'''
    String
    Use this to find parlindrom:

        while left >= 0 and right < len(ss) and ss[left] == ss[right]:
            left -= 1
            right += 1
            # Find a parlindrom
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        def countParlindrom(left, right, ss):
            cnt = 0
            while left >= 0 and right < len(ss) and ss[left] == ss[right]:
                left -= 1
                right += 1
                cnt += 1
            
            return cnt
        
        ans = 0
        for i in range(len(s)):
            ans += countParlindrom(i, i, s)
            ans += countParlindrom(i, i+1, s)
        
        return ans