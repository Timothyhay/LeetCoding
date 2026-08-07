target_dict = {'a': 1, 'b': 2, 'c': 7, 'e': 5, 'f': 5, 'eee': 5}
# Method 1
sd = sorted(target_dict.items(), key=lambda x: (x[1], x[0]))
print(sd)
sd2 = sorted(target_dict.items(), key=lambda x: x[1])
print(sd2)
