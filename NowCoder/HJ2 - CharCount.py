import sys
from collections import defaultdict


s = input().lower()
target = input().lower()

h = defaultdict(int)
for c in s:
    h[c] += 1

print(h[target])

'''
print(s.count(target))
'''