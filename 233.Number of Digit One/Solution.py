class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        ans = 0
        base = 1
        last = 0
        while n:
            t = n%10
            n = n/10
            if t > 1:
                ans = ans + (n+1)*base
            elif t == 1:
                ans = ans + n*base + last + 1
            else:
                ans = ans + n*base
            last = t*base + last
            base = base*10
        return ans