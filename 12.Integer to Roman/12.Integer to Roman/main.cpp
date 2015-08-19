//
//  main.cpp
//  12.Integer to Roman
//
//  Created by Simon Xu on 8/19/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <iostream>
#include "Solution.cpp"

int main(int argc, const char * argv[]) {
    Solution *S = new Solution();
    string result = S->intToRoman(123);
    cout << result << endl;
    return 0;
}
