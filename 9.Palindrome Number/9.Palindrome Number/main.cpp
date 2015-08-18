//
//  main.cpp
//  9.Palindrome Number
//
//  Created by Simon Xu on 8/18/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <iostream>
#include "Solution.cpp"
int main(int argc, const char * argv[]) {
    Solution *S = new Solution();
    bool B = S->isPalindrome(-123321);
    cout << B;
    return 0;
}
