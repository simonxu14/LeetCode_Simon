//
//  main.cpp
//  5.Longest Palindromic Substring
//
//  Created by Simon Xu on 8/15/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <iostream>
#include "Solution.cpp"

int main(int argc, const char * argv[]) {
    Solution *S = new Solution();
    string result = S->longestPalindrome("aa");
    cout << result;
    return 0;
}
