//
//  Solution.cpp
//  136.Single Number
//
//  Created by Simon Xu on 9/14/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int index = 0;
        for (int i = 0; i<nums.size(); i++) {
            index = index ^ nums[i];
        }
        return index;
    }
};