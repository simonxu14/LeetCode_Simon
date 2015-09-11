//
//  Solution.cpp
//  53.Maximum Subarray
//
//  Created by Simon Xu on 9/10/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>
#include <vector>

using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
//        int *MAX = new int[nums.size()];
//        MAX[0] = 0;
//        for (int i = 1; i <= nums.size(); i++) {
//            MAX[i] = max(MAX[i-1], MAX[i-1] + nums[i-1]);
//            if (MAX[i] < 0) {
//                MAX[i] = 0;
//            }
//        }
//        return MAX[nums.size()];
        int sum = 0;
        int max = INT_MIN;
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            if (sum > max) {
                max = sum;
            }
            if (sum < 0) {
                sum = 0;
            }
        }
        return max;
    }
};