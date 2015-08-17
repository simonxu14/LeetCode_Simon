//
//  main.cpp
//  7.Reverse Integer
//
//  Created by Simon Xu on 8/17/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <iostream>
#include "Solution.cpp"

int main(int argc, const char * argv[]) {
    Solution *S = new Solution();
    int result = S->reverse(-2147483648);
    cout << result;
    return 0;
}
