#coding = utf-8
class Solution(object):
    def longestCommonPrefix(self, strs):
        length = len(strs)
        if length == 0:
            return ""
        elif length == 1:
            return strs[0]
        else:
            result = strs[0]
            for i in range(1, length):
                if strs[i] == "":
                    return ""
                while result != strs[i][:len(result)]:
                    result_len = len(result)
                    result = result[:result_len - 1]
                    print result
                    if result == "":
                        return ""
            return result

Sol = Solution()
result = Sol.longestCommonPrefix(["a","b"])
print result