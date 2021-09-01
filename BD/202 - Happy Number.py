# BD - 202

from typing import List


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                sum += digit ** 2
            n = sum

        return n == 1

