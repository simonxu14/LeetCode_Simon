//
//  Solution.cpp
//  6.ZigZag Conversion
//
//  Created by Simon Xu on 8/16/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        string result;
        int index = 0;
        int k = 0;
        if (s.size() == 0 || numRows == 1 || s.size() <= numRows) {
            return s;
        }
        for (int i = 0; i < numRows; i++) {
            index = 0;
            for (int j = i; j < s.size(); j = j + 2*numRows - 2) {
                if (i == 0 || i == numRows - 1 ) {
                    result.append(1, s[j]);
//                    cout << "AAA  " << result << endl;
                }
                else {
                    result.append(1, s[j]);
//                    cout << "BBB  " << result << endl;
                    k = numRows * (2 * index + 1) - 1 - 2 * index;
                    if (j + 2 * (k - j) >= s.size()) {
                        break;
                    }
                    else {
                        result.append(1, s[j + 2 * (k - j)]);
//                        cout << "CCC  " << result << endl;
                    }
                }
                index ++;
            }
        }
        return result;
    }
};