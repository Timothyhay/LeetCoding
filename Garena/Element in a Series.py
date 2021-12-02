# https://www.geeksforgeeks.org/find-n-th-element-series-2-digits-4-7-allowed/

# 4, 7, 44, 47, 74,...... 44744,.. etc. N <= 1000

class Solution:
    def NthTermOfSeries(self, N):
        hashlist = [0] * (n + 1)
        hashlist[1] = 4
        hashlist[2] = 7
        for i in range(3, N+1):
            if i % 2 == 1:
                hashlist[i] = hashlist[i // 2] * 10 + 4
            else:
                hashlist[i] = hashlist[i // 2 - 1] * 10 + 7

        return hashlist[N]

'''
The idea is based on the fact that the value of last digit alternates in series. For example, if last digit of i-th number is 4, then last digit of (i-1)-th and (i+1)-th numbers must be 7.
We create an array of size (n+1) and push 4 and 7 (These two are always first two elements of series) to it. For more elements we check 
1) If i is odd, 
      arr[i] = arr[i/2]*10 + 4; 
2) If it is even, 
      arr[i] = arr[(i/2)-1]*10 + 7; 
At last return arr[n].
'''

if __name__ == '__main__':
    s = Solution()
    print(s.NthTermOfSeries(19))




