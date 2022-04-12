'''
Array 2

One method:
十进制转为任意进制:
这个数对基数依次取余，将余数倒序输出，在倒序输出余数之前正序输出最后一次的商。（这个方法是很简单的一种方式，可以大大的节省时间）

将十进制转成八进制
579 / 8 = 72　．．．３
72 / 8 =9　．．．0
9 / 8 =1　．．．１

先输出最后一次计算的商，然后倒序从下到上输出余数
八进制的 576 为　1103
'''

'''
Here we use Add2Binary method - but multiply -1 to each carry

'''
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        ans = []
        carry = 0
        while arr1 or arr2 or carry:
            carry += (arr1 or [0]).pop() + (arr2 or [0]).pop()
            # ans.append(carry % 2)
            ans.append(carry & 1)
            # carry = int(carry / -2)
            carry = -(carry >> 1)
        
        while len(ans) > 0 and ans[-1] == 0:
            ans.pop()
        if len(ans) == 0:
            return [0]
        
        return ans[::-1]
