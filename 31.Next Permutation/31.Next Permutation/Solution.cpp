//
//  Solution.cpp
//  31.Next Permutation
//
//  Created by Simon Xu on 9/6/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        bool possible = false;
        for (int i = nums.size() - 1; i > 0; i--) {
            if (nums[i] > nums[i-1]) {
                for (int j = nums.size() - 1; j > 0; j--) {
                    if (nums[j] > nums[i-1]) {
                        swap(nums[i-1], nums[j]);
                        for (int m = i, n = nums.size() - 1; m < n; m++, n--) {
                            swap(nums[m], nums[n]);
                        }
                        break;
                    }
                }
                possible = true;
                break;
            }
        }
        if (!possible) {
            for (int q = 0, p = nums.size() - 1; q < p; q++, p--) {
                swap(nums[q], nums[p]);
            }
        }
    }
};