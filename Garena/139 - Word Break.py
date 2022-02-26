from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        match = [False for _ in range(len(s)+1)]
        match[0] = True

        for i in range(len(s)+1):
            for word in wordDict:
                if match[i-len(word)] == True and s[i-len(word):i] == word:
                    match[i] = True
                    break

        return match[-1]

if __name__ == '__main__':
    S = Solution()
    worddict = ["leet","code"]
    print(S.wordBreak("leetcode", worddict))