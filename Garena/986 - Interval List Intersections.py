class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        f = 0
        s = 0
        ans = []
        while f < len(firstList) and s < len(secdonList):
            low = max(firstList[f][0], secondList[s][0])
            high = min(firstList[f][1], secondList[s][1])
            if low <= high:
                ans.append([low, high])

            if firstList[f][1] < secondList[s][1]:
                f += 1
            else:
                s += 1

        return ans