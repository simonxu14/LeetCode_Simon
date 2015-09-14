//
//  Solution.cpp
//  198.House Robber
//
//  Created by Simon Xu on 9/13/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        vector<int> sum = *new vector<int>(nums.size()+1);
        if (nums.size() == 0) {
            return 0;
        }
        sum[0] = 0;
        sum[1] = nums[0];
        for (int i = 2; i <= nums.size(); i++) {
            sum[i] = sum[i-1] > sum[i-2] + nums[i-1]? sum[i-1] : sum[i-2] + nums[i-1];
        }
        
        return sum[nums.size()];
    }
};