//
//  Solution.cpp
//  217.Contains Duplicate
//
//  Created by Simon Xu on 9/14/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> map;
        for(int i:nums)
        {
            if(map.find(i)!=map.end())
                return true;
            map[i];
        }
        return false;
    }
};