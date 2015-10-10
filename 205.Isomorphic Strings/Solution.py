__author__ = 'Simon'
class Solution(object):
    # Your runtime beats 3.93% of python submissions.
    # def isIsomorphic(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: bool
    #     """
    #     map = {}
    #     if len(s) != len(t):
    #         return False
    #     if len(s) == 0:
    #         return True
    #     map[s[0]] = t[0]
    #     index = 1
    #     while index < len(s):
    #         if s[index] not in map.keys():
    #             if t[index] in map.values():
    #                 return False
    #             else:
    #                 map[s[index]] = t[index]
    #         else:
    #             if t[index] not in map.values():
    #                 return False
    #             else:
    #                 if map.get(s[index]) != t[index]:
    #                     return False
    #         index += 1
    #     return True

    def isIsomorphic(self, s,t):
        ds, dt= {}, {}
        if len(s) != len(t):
            return False
        for i in xrange(len(s)):
            if s[i] in ds:
                ds[s[i]] += [i]
            else:
                ds[s[i]] = [i]
            if t[i] in dt:
                dt[t[i]] += [i]
            else:
                dt[t[i]] = [i]
        return sorted(ds.values()) == sorted(dt.values())