//
//  Solution.cpp
//  7.Reverse Integer
//
//  Created by Simon Xu on 8/17/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

class Solution {
public:
    int reverse(int x) {
        bool positive = true;
        if (x < 0) {
            positive = false;
            x = x * (-1);
        }
        if (x == 0) {
            return 0;
        }
        stringstream ss;
        ss << x;
        string number = ss.str();
        string number_reverse;
        
        int length = static_cast<int>(number.size());
        int i;
        for (i = length - 1; i >= 0; i--) {
            number_reverse.append(1, number[i]);
        }
        stringstream ss2;
        ss2 << number_reverse;
        int result;
        ss2 >> result;
        if (result == (numeric_limits<int>::max)()) {
            return 0;
        }
        if (!positive) {
            result = result * (-1);
        }
        return result;
    }
};