__author__ = 'Simon'
class Solution(object):
    def findSubstring(self, s, W):
        wordNum = len(W)
        wordCount = {}
        for i in W:
            if i not in wordCount:
                wordCount[i] = 1
            else:
                wordCount[i] += 1
        wordLen = len(W[0])
        result = []
        for j in range(len(s) + 1 - wordLen * wordNum):
            m = 0
            current = {}
            while m < wordNum:
                word = s[j+m*wordLen : j+m*wordLen+wordLen]
                if word not in wordCount:
                    break
                if word not in current:
                    current[word] = 1
                else:
                    current[word] += 1
                if current[word] > wordCount[word]:
                    break
                m += 1
            if m == wordNum:
                result.append(j)
        return result