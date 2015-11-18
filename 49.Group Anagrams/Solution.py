__author__ = 'Simon'
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 0 or strs[0] == "":
            return []
        dict = {}
        result = []
        for item in strs:
            item_ele = tuple(sorted(item))
            if item_ele not in dict.keys():
                dict[item_ele] = [item]
            else:
                dict[item_ele].append(item)
        for key in dict:
            item_array = dict[key]
            result.append(item_array)
        return result





# class Solution(object):
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
#         mydict = dict()
#         results = []
#         for item in strs:
#             item_ele = tuple(sorted(item))
#             if not item_ele in mydict:
#                 mydict[item_ele] = [item]
#             else:
#                 mydict[item_ele].append(item)
#         for key in mydict:
#             item_array = mydict[key]
#             item_array.sort()
#             results.append(item_array)
#         return results