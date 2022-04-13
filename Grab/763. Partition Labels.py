'''
    String
    Greedy

    For each letter encountered, process the last occurrence of that letter, extending the current partition [start, end] appropriately.
'''

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = dict()
        for i in range(len(s)-1, -1, -1):
            if s[i] not in last_index:
                last_index[s[i]] = i
        
        ans = []
        start = 0
        end = -1
        for i in range(len(s)):
            if last_index[s[i]] > end:
                end = last_index[s[i]]
            if i == end:
                ans.append(end - start + 1)
                start = i + 1
        return ans