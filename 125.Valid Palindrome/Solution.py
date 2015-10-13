__author__ = 'Simon'
class Solution(object):
    # def isPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: bool
    #     """
    #     s.lower()
    #     i = 0
    #     j = len(s) - 1
    #     while i < j:
    #         while not s[i].isalpha():
    #             i += 1
    #             if i >= j:
    #                 return True
    #         while not s[j].isalpha():
    #             j -= 1
    #             if i >= j:
    #                 return True
    #         if s[i] != s[j]:
    #             return False
    #     return True

    def isPalindrome(self, s):
        if not s:
            return True
        s=s.lower()
        s1=[]
        for x in range(len(s)):
            if s[x].isalpha() or s[x].isdigit():
                s1.append(s[x])     #Get s1 with letters and digits only
        for i in range(int(len(s1)/2)):
            if not s1[i]==s1[-i-1]:
                return False
        return True