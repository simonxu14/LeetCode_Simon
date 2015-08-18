//
//  Solution.cpp
//  9.Palindrome Number
//
//  Created by Simon Xu on 8/18/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        string number;
        stringstream ss;
        ss << x;
        number = ss.str();
        int i;
        int j;
        for (i = static_cast<int>(number.size()) - 1, j = 0; j <= i; i--, j++) {
            if (number[j] != number[i]) {
                return false;
            }
        }
        return true;
    }
};