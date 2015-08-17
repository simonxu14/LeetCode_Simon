//
//  main.cpp
//  6.ZigZag Conversion
//
//  Created by Simon Xu on 8/16/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <iostream>
#include "Solution.cpp"

int main(int argc, const char * argv[]) {
    Solution *S =  new Solution();
    string result = S->convert("ABCDE", 4);
    cout << result << endl;
//    for (int i = 0; i < result.size(); i++) {
//        cout << result[i] << endl;
//    }
    return 0;
}
