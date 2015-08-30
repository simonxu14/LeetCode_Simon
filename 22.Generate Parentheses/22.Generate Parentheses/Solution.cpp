//
//  Solution.cpp
//  22.Generate Parentheses
//
//  Created by Simon Xu on 8/29/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
//    vector<string> generateParenthesis(int n) {
//        vector<string> result;
//        vector<string> current;
//        if (n == 0) {
//            return result;
//        }
//        result.push_back("()");
//        n = n - 1;
//        while (n > 0) {
//            for (int i = 0; i < result.size(); i++) {
//                current.push_back('(' + result[i] + ')');
//            }
//            for (int j = 0; j < result.size(); j++) {
//                if (j == result.size() - 1) {
//                    current.push_back(result[j] + "()");
//                    break;
//                }
//                current.push_back(result[j] + "()");
//                current.push_back("()" + result[j]);
//            }
//            result.clear();
//            result = current;
//            current.clear();
//            n--;
//        }
//        return result;
//    }
//};

void CombinationPar(vector<string>& result, string& sample, int deep, int n, int leftNum, int rightNum)
{
    if(deep == 2*n)
    {
        result.push_back(sample);
        return;
    }
    if(leftNum<n)
    {
        sample.push_back('(');
        CombinationPar(result, sample, deep+1, n, leftNum+1, rightNum);
        sample.resize(sample.size()-1);
    }
    if(rightNum<leftNum)
    {
        sample.push_back(')');
        CombinationPar(result, sample, deep+1, n, leftNum, rightNum+1);
        sample.resize(sample.size()-1);
    }
}
vector<string> generateParenthesis(int n) {
    // Start typing your C/C++ solution below
    // DO NOT write int main() function
    vector<string> result;
    string sample;
    if(n!= 0)
        CombinationPar(result, sample, 0, n, 0, 0);
    return result;
}
};