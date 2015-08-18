//
//  Solution.cpp
//  8.String to Integer (atoi)
//
//  Created by Simon Xu on 8/17/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <math.h>
#include <sstream>

using namespace std;

//class Solution {
//public:
//    int myAtoi(string str) {
//        int result = 0;
//        int i;
//        int j;
//        if (str[0] == '-') {
//            for (i = static_cast<int>(str.size()) - 1, j = 1; i >= 1; i--, j++) {
//                result = result + str[i] * j;
//                result = result * (-1);
//            }
//        }
//        else {
//            for (i = static_cast<int>(str.size()) -1, j = 0; i >= 0; i--, j++) {
//                result = result + (int)str[i] * pow(10, j);
//            }
//        }
//        return result;
//    }
//};

class Solution {
public:
    int myAtoi(string str) {
        if (str.size() == 0) {
            return 0;
        }
        stringstream ss;
        ss << str;
        int result;
        ss >> result;
        return result;
    }
};

//numeric_limits<int>::max