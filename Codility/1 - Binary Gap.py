
def solution(N):
    binNum = bin(N)[2:]
    maxGap = 0
    crtGap = 0
    head = False

    for c in binNum:
        if c == '1':
            if head == False:
                head = True
                continue
            elif head == True:
                maxGap = max(maxGap, crtGap)
                crtGap = 0
        else:
            crtGap += 1

    return maxGap


