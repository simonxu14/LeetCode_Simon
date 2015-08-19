//
//  main.cpp
//  13.Roman to Integer
//
//  Created by Simon Xu on 8/19/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <iostream>
#include "Solution.cpp"

int main(int argc, const char * argv[]) {
    Solution *S = new Solution();
    int result;
    result = S->romanToInt("IV");
    cout << result << endl;
    return 0;
}
