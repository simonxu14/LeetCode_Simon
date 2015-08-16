//
//  Solution.cpp
//  5.Longest Palindromic Substring
//
//  Created by Simon Xu on 8/15/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

//class Solution {
//public:
//    string longestPalindrome(string s) {
//        int string_length = static_cast<int>(s.size());
//        
//        string result = "";
//        string current_odd = "";
//        string current_even = "";
//        int current_length = 0;
//        int max_length = 0;
//        int n;
//        
//        //odd number
//        for (int i = 0; i < string_length; i++) {
//            n = 1;
//            current_odd = s[i];
//            current_length = 1;
//            while (s[i-n] == s[i+n]) {
//                current_odd = s[i-n] + current_odd;
//                current_odd = current_odd + s[i+n];
//                n ++;
//                current_length = current_length + 2;
//            }
//            if (current_length > max_length) {
//                max_length = current_length;
//                result = current_odd;
//            }
//        }
//        
//        //even number
//        for (int j = 0; j < string_length; j++) {
//            if (s[j] == s[j+1]) {
//                n = 1;
//                current_even = s[j];
//                current_even = current_even + s[j+1];
//                current_length = 2;
//                while (s[j-n] == s[j+n+1]) {
//                    current_even = s[j-n] + current_even;
//                    current_even = current_even + s[j+n+1];
//                    n ++;
//                    current_length = current_length + 2;
//                }
//                if (current_length > max_length) {
//                    max_length = current_length;
//                    result = current_even;
//                }
//            }
//        }
//        return result;
//    }
//};



class Solution {
public:
    string longestPalindrome(string s) {
        bool P[1000][1000];
        int len = 0;
        int max = 0;
        int max_i = 0;
        int max_j = 0;
        
        for (int m = 0; m < s.size(); m++) {
            P[m][m] = true;
            max = 1;
            max_i = m;
            max_j = m;
        }
        for (int n = 0; n < s.size(); n++) {
            if (s[n] == s[n+1]) {
                P[n][n+1] = true;
                max = 2;
                max_i = n;
                max_j = n + 1;
            }
            else P[n][n+1] = false;
        }
        for (int j = 2; j < s.size(); j++) {
            for (int i = 0; i <= j - 2; i++) {
                P[i][j] = P[i+1][j-1] && (s[i] == s[j]);
                
                if (P[i][j]) {
//                    cout << i << " " << j << " " << P[i][j] << endl;
                    len = j - i + 1;
                    if (len > max) {
                        max = len;
                        max_i = i;
                        max_j = j;
                    }
                }
            }
        }
//        cout << max_i << " " << max_j << endl;
        string result;
        for (int k = max_i; k <= max_j; k++) {
            result = result + s[k];
        }
        return result;
    }
};


