//
//  main.cpp
//  3.Longest Substring
//
//  Created by Simon Xu on 8/13/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <iostream>
#include "Solution.cpp"

int main(int argc, const char * argv[]) {
    Solution *S = new Solution();
    string s = "cdd";
    int result = S->lengthOfLongestSubstring(s);
    cout << result;
    return 0;
}
