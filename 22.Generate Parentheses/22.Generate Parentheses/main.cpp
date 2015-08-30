//
//  main.cpp
//  22.Generate Parentheses
//
//  Created by Simon Xu on 8/29/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <iostream>
#include "Solution.cpp"

int main(int argc, const char * argv[]) {
    Solution *S = new Solution();
    vector<string> result = S->generateParenthesis(3);
    for (int m = 0; m < result.size(); m ++) {
        cout << result[m] << endl;
    }
    return 0;
}
