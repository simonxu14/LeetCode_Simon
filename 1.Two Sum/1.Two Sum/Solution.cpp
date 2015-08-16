//
//  Solution.cpp
//  1.Two Sum
//
//  Created by Simon Xu on 8/11/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

//O(n*n)
//class Solution{
//public:
//    vector<int> twoSum(vector<int>& nums, int target){
//        int m,n;
//        vector<int> result;
//        for (m = 0; m < nums.size(); m ++) {
//            for (n = m + 1; n < nums.size(); n ++) {
//                if (nums[m] + nums[n] == target) {
//                    result.push_back(m + 1);
//                    result.push_back(n + 1);
//                    break;
//                }
//            }
//        }
//        return result;
//    }
//};

//O(n)
class Solution{
public:
    vector<int> twoSum(vector<int>& nums, int target){
        map<int, int> mapping;
        vector<int> result;
        for (int n = 0; n < nums.size(); n ++) {
            if (mapping.find(nums[n]) != mapping.end()) {
                result.push_back(mapping[nums[n]] + 1);
                result.push_back(n + 1);
                break;
            }
            else mapping[target - nums[n]] = n;
        }
        return result;
    }
};