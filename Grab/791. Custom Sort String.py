'''
    Custom Sort String
    Sort as given pattern

    Traverse the pattern string and print amount*char

'''

from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans = ""
        cnt = Counter(s)
        for c in order:
            if c in cnt:
                ans += cnt[c] * c
                cnt.pop(c)
        
        for c in cnt:
            ans += cnt[c] * c
        
        return ans