//
//  Solution.cpp
//  3.Longest Substring
//
//  Created by Simon Xu on 8/13/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <cstring>
#include <iostream>
#include <map>
using namespace std;

//class Solution {
//public:
//    int lengthOfLongestSubstring(string s) {
//        int string_l = static_cast<int>(s.size());
//        int max_length;
//        int current_length;
//        string current_string;
//        
//        if (s == "") {
//            return 0;
//        }
//        
//        max_length = 1;
//        current_length = 1;
//        current_string = s[0];
//        cout << current_string << endl;
//        
//        for (int m = 1; m < string_l; m++) {
//            if (find(current_string.begin(), current_string.end(),s[m]) == current_string.end()) {
//                current_string.insert(current_string.end(), s[m]);
//                cout << current_string << endl;
//                current_length ++;
//                if (max_length < current_length) {
//                    max_length = current_length;
//                }
//            }
//            else {
//                cout << 'Q' << endl;
//                current_string.erase(current_string.begin(), find(current_string.begin(), current_string.end(),s[m]) + 1);
//                current_string.insert(current_string.end(), s[m]);
//                cout << current_string << endl;
//                current_length = static_cast<int>(current_string.size());
//                if (max_length < current_length) {
//                    max_length = current_length;
//                }
//            }
//        }
//        return max_length;
//    }
//};

//class Solution {
//public:
//    int lengthOfLongestSubstring(string s) {
//        map<char, int> mapping;
//        int string_l = static_cast<int>(s.size());
//        int max_length;
//        int current_length;
//        int current_head;
//        if (s == "") {
//            return 0;
//        }
//        max_length = 1;
//        current_length = 1;
//        current_head = 0;
//        mapping.insert(pair<char, int>(s[0], 0));
//        
//        for (int m = 1; m < string_l; m++) {
//            if (mapping.find(s[m]) == mapping.end()) {
//                mapping. insert(pair<char, int>(s[m],m));
//                current_length ++;
//                map<char,int>::iterator it;
//                for(it=mapping.begin();it!=mapping.end();++it)
//                    cout<<"key: "<<it->first <<" value: "<<it->second<<endl;
//                cout << "********" <<endl;
//                if (max_length < current_length) {
//                    max_length = current_length;
//                }
//            }
//            else {
//                mapping.erase(mapping.find(s[m]), mapping.end());
//                mapping.insert(pair<char, int>(s[m], m));
//                current_length = static_cast<int>(mapping.size());
//                if (max_length < current_length) {
//                    max_length = current_length;
//                }
//            }
//        }
//        return max_length;
//    }
//};

//class Solution {
//public:
//    int lengthOfLongestSubstring(string s) {
//        int string_l = static_cast<int>(s.size());
//        int count[26];
//        int current_l = 0;
//        int max_l = 0;
//        memset(count, -1, sizeof(int)*26);
//        for (int m = 0; m < string_l; m++) {
//            if (count[s[m] - 'a'] >= 0 ) {
//                m = count[s[m] - 'a'];
//                current_l = 0;
//                memset(count, -1, sizeof(int)*26);
//            }
//            else {
//                count[s[m] - 'a'] = m;
//                current_l = current_l + 1;
//                if(current_l > max_l) {
//                    max_l = current_l;
//                }
//            }
//        }
//        return max_l;
//    }
//};



class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = static_cast<int>(s.length());
        int i = 0, j = 0;
        int maxLen = 0;
        bool exist[256] = { false };
        while (j < n) {
            if (exist[s[j]]) {
                maxLen = max(maxLen, j-i);
                while (s[i] != s[j]) {
                    exist[s[i]] = false;
                    i++;
                }
                i++;
                j++;
            }
            else {
                exist[s[j]] = true;
                j++;
            }
        }
        maxLen = max(maxLen, n-i);
        return maxLen;
    }
};

//    string s = "pwwkew";
//    string s = "abcabcbb";
//    string s = "ynyo";