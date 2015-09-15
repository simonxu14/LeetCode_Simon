__author__ = 'Simon'
class Solution(object):
    def isAnagram(self, s, t):
        # result = 1
        # i = 0
        # if len(s) != len(t):
        #     result = 0
        #     return result == 1
        # while i < len(t):
        #     if i == len(t)-1:
        #         if s[i] != t[i]:
        #             result = 0
        #             break
        #         else:
        #             break
        #     if s[i] != t[i+1]:
        #         result = 0
        #         break
        #     i += 2
        # j = 1
        # while j < len(t):
        #     if s[j] != t[j-1]:
        #         result = 0
        #         break
        #     j += 2
        # return result == 1

        # result = 1
        # if len(s) !=  len(t):
        #     result = 0
        #     return result == 1
        # m = [0 for i in range(26)]
        # for i in range(len(s)):
        #     m[s[i]-'a'] += 1
        # for j in range(len(t)):
        #     m[t[i]-'a'] -= 1
        #     if m[t[i]-'a'] < 0:
        #         result = 0
        # return result ==1

        return sorted(s) == sorted(t)