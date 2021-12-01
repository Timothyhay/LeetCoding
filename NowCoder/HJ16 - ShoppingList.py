# If you need to import additional packages or classes, please import here.
def findAns(s, cnt, tlen):
    # init: s = '1'
    clen = len(s)
    cnt = 0
    for c in range(clen):
        cnt += int(s[c])
        if cnt < 0:
            return 0
    if clen >= tlen and cnt == 0:
        return 1
    if cnt < 0:
        return 0
    p = s.copy()
    p.append(1)
    m = s.copy()
    m.append(-1)
    return findAns(p, cnt + 1, tlen) + findAns(m, cnt - 1, tlen)


def func():
    sum = 0
    t = int(input())
    if t % 2 != 0:
        print(0)
    else:
        cnt = 1
        minus = t / 2
        plus = t / 2 - 1
        # 2:1, 4:++-- +-+-
        '''
        s = [0] * len(t)
        s[0] = 1
        ser = []
        for i in range(1, len(t)):
            tsum = 0
            for j in range(0, i):
                tsum += s[j]
            if tsum > 0:
                ser.append()
        '''

        # print(t)
        print(findAns([1], 1, t))

    # please define the python3 input here. For example: a,b = map(int, input().strip().split())
    # please finish the function body here.
    # please define the python3 output here. For example: print().


if __name__ == "__main__":
    func()
