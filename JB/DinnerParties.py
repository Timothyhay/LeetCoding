'''
    Recurively find a combination of fix-size chars

'''
def find_party(friends, table_size):
    ans = []
    def combination(pos=0, group=[]):
        if len(group) == table_size:
            ans.append(group)
            return
        if pos < len(friends):
            # Option 1: skip crt value
            combination(pos + 1, group)

            # Option 2: include crt value
            new_group = list(group)
            new_group.append(friends[pos])
            combination(pos + 1, new_group)

    combination(0, [])
    print(len(ans), ans)


find_party("ABCDE", 3)
