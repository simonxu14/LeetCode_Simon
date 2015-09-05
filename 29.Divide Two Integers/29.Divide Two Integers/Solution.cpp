//
//  Solution.cpp
//  29.Divide Two Integers
//
//  Created by Simon Xu on 9/5/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <math.h>

using namespace std;

class Solution {
public:
    int divide(long long dividend, long long divisor) {
        if (dividend == 0 || divisor == 0) {
            return 0;
        }
        int positive = 0;
        unsigned long long _dividend = abs(dividend);
        unsigned long long _divisor = abs(divisor);
        unsigned long long _result;
        if ((dividend >= 0 && divisor >= 0) || (dividend <= 0 && divisor <= 0)) {
            positive = 1;
        }
        _result = sub_divide(_dividend, _divisor);
        if (positive) {
            if (_result > INT_MAX) {
                return INT_MAX;
            }
            return _result;
        }
        else {
            if (_result > INT_MAX) {
                return INT_MIN;
            }
            return -_result;
        }
    }
    
    int sub_divide(long long left, long long divisor) {
        if (left < divisor) {
            return 0;
        }
        long long temp = divisor;
        int index = 0;
        while (left >= temp) {
            temp = temp << 1;
            index++;
        }
        return pow(2, index-1) + sub_divide(left - (temp>>1), divisor);
    }
};