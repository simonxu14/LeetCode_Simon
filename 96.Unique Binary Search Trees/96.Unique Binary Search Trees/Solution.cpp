//
//  Solution.cpp
//  96.Unique Binary Search Trees
//
//  Created by Simon Xu on 9/14/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int numTrees(int n) {
        vector<int> sum = *new vector<int>(n+1);
        sum[0] = 1;
        sum[1] = 1;
        for (int i = 2; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                sum [i] = sum[i] + sum[j] * sum[i - j -1];
            }
        }
        return sum[n];
    }
};