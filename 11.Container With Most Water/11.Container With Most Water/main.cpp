//
//  main.cpp
//  11.Container With Most Water
//
//  Created by Simon Xu on 8/18/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <iostream>
#include "Solution.cpp"

int main(int argc, const char * argv[]) {
    Solution *S = new Solution();
    vector<int> v = {1, 2, 4, 3};
    int result = S -> maxArea(v);
    cout << result << endl;
    return 0;
}
