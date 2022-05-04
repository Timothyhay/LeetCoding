'''
Start from the end and look for increasing pattern, it our case 7641.
If it happen, that all number has increasing pattern, there is no bigger number with the same digits, so we can return -1.
Now, we need to find the first digit in our ending, which is less or equal to digits[i-1]:
 we have ending 5 7641 and we are looking for the next number with the same digits.
  What can go instead of 5: it is 6!
   Let us SWAP these two digits, so we have 6 7541 now. Finally, we need to reverse last ditits to get 6 1457 as our ending.
Complexity: time complexity is O(m), where m is number of digits in our number, space complexity O(m) as well.

'''

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        i = len(digits) - 1
        while i - 1 >= 0 and digits[i] <= digits[i - 1]:
            i -= 1

        if i == 0: return -1

        j = i
        while j + 1 < len(digits) and digits[j + 1] > digits[i - 1]:
            j += 1

        digits[i - 1], digits[j] = digits[j], digits[i - 1]
        digits[i:] = digits[i:][::-1]
        ret = int(''.join(digits))

        return ret if ret < 1 << 31 else -1