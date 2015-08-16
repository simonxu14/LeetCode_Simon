//
//  main.cpp
//  1.Two Sum
//
//  Created by Simon Xu on 8/11/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include "Solution.cpp"

int main(int argc, const char * argv[]) {
    Solution S;
    vector<int> input = {2,3,4};
    vector<int> result = S.twoSum(input, 6);
    cout << result[0] << result[1];
    return 0;
}
