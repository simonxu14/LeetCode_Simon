class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        temp = {}
        for i in range(len(nums)):
            if nums[i] in temp.keys():
                temp[nums[i]] += 1
            else:
                temp[nums[i]] = 1
        for k in temp.keys():
            if temp[k] > len(nums) / 3:
                res.append(k)
        return res


        # tmp = {}
        # res = []
        # for n in list(set(nums)):
        #     tmp[n] = nums.count(n)
        # for k,v in tmp.iteritems():
        #     if v > len(nums) / 3:
        #         res.append(k)
        # return res