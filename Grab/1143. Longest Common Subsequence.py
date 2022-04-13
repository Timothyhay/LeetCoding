'''
	String 3
	DP
	State Transition Equation: 

	DP[r][c] = {  0 							if c == 0 or r == 0;
				  DP[r-1][c-1] + 1 				if t1[r] == t2[c];
				  max(DP[r-1][c], DP[r][c-1])	if t1[r] != t2[c]}

	Since we leave empty-string col&row = 0, store result of (t1[r] == t2[c]) at lcs[t2 + 1][t1 + 1].
	That is:
	
        if text2[t2] == text1[t1]:
            lcs[t2 + 1][t1 + 1] = lcs[t2][t1] + 1
        else:
            lcs[t2 + 1][t1 + 1] = max(lcs[t2 + 1][t1], lcs[t2][t1 + 1])
        
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lcs = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]
        for t2 in range(len(text2)):
            for t1 in range(len(text1)):
                if text2[t2] == text1[t1]:
                    lcs[t2 + 1][t1 + 1] = lcs[t2][t1] + 1
                else:
                    lcs[t2 + 1][t1 + 1] = max(lcs[t2 + 1][t1], lcs[t2][t1 + 1])
        
        return lcs[len(text2)][len(text1)]
            