import sys

for line in sys.stdin:
    try:
        ans = sorted(list(set(line.strip())), key=lambda x: line.count(x) * 1000 - ord(x), reverse=True)
        print("".join(ans))
#         print(ans)
    except:
        break

'''
c = collections.Counter(s)
sorted_items = sorted(c.items(), key=lambda x: (-x[1], x[0]))
print(''.join([item[0] for item in sorted_items]))
'''
