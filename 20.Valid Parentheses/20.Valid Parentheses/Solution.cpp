//
//  Solution.cpp
//  20.Valid Parentheses
//
//  Created by Simon Xu on 8/27/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>
#include <stack>
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<int> stk;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') {
                stk.push(1);
            }
            if (s[i] == '{') {
                stk.push(2);
            }
            if (s[i] == '[') {
                stk.push(3);
            }
            if (s[i] == ')') {
                if (stk.empty()) {
                    return false;
                }
                if(stk.top() == 1) {
                    stk.pop();
                }
                else return false;
            }
            if (s[i] == '}') {
                if (stk.empty()) {
                    return false;
                }
                if(stk.top() == 2) {
                    stk.pop();
                }
                else return false;
            }
            if (s[i] == ']') {
                if (stk.empty()) {
                    return false;
                }
                if(stk.top() == 3) {
                    stk.pop();
                }
                else return false;
            }
        }
        if (stk.empty()) {
            return true;
        }
        return false;
    }
};