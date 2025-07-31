class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        if x < -(2**31) or x > 2**31-1:
            return 0
        n = False
        if x < 0:
            x *= -1
            n = True
        sym = "" if n is False else "-"
        y = int(sym + str(x)[::-1].lstrip('0'))
        if y < -(2**31) or y > 2**31-1:
            return 0
        return y
        
