'''
Explanation
base2 function is quite basis of basis.

check last digit by N%2 or N&1.
If it's 1, you get 1.
If it's 0, you get 0.

shift to right N >> 1.
This actually do two things:
2.1 Minus 1 if last digit is 1.
2.2 Divide N by 2.

base -2 is no difference,
except that we need divide N by -2.

'''

def toBase2(n):
    res = ""
    while n:
        res = str(n & 1) + res
        n = n >> 1

    if res == "":
        return "0"
    else:
        return res

def baseNeg2(self, n: int) -> str:
    res = ""
    while n:
        res = str(n & 1) + res
        n = -(n >> 1)

    if res == "":
        return "0"
    else:
        return res


if __name__ == '__main__':
    print(toBase2(2))