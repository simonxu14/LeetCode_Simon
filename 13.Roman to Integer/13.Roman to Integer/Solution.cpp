//
//  Solution.cpp
//  13.Roman to Integer
//
//  Created by Simon Xu on 8/19/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    int result = 0;
    int temp = 0;
    int romanToInt(string s) {
        for (int n = static_cast<int>(s.size()) - 1; n >= 0; n--) {
            if (s[n] == 'I') {
                if (s[n+1] == 'V' || s[n+1] == 'X') {
                    result = result - 1;
                } else {
                    result = result + 1;
                }
            }
            if(s[n] == 'V') {
                result = result + 5;
            }
            
            if (s[n] == 'X') {
                if (s[n+1] == 'L' || s[n+1] == 'C') {
                    result = result - 10;
                } else {
                    result = result + 10;
                }
            }
            if(s[n] == 'L') {
                result = result + 50;
            }
            
            if (s[n] == 'C') {
                if (s[n+1] == 'D' || s[n+1] == 'M') {
                    result = result - 100;
                } else {
                    result = result + 100;
                }
            }
            if(s[n] == 'D') {
                result = result + 500;
            }
            
            if (s[n] == 'M') {
                result = result + 1000;
            }
        }
        return result;
    }
};