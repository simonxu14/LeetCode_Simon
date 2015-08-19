//
//  Solution.cpp
//  11.Container With Most Water
//
//  Created by Simon Xu on 8/18/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;

//class Solution {
//public:
//    int maxArea(vector<int>& height) {
//        if (height.size() == 0 || height.size() == 1) {
//            return 0;
//        }
//        int area = 0;
//        int temp = 0;
//        for (int n = 0; n < height.size(); n++) {
//            for (int m = n - 1; m >= 0; m--) {
//                temp = (height[n] + height[m]) * (n - m)/2;
//                if (temp > area) {
//                    area = temp;
//                }
//            }
//        }
//        return area;
//    }
//};

class Solution {
public:
    int maxArea(vector<int>& height) {
        if (height.size() == 0 || height.size() == 1) {
            return 0;
        }
        int area = 0;
        int temp = 0;
        int j = static_cast<int>(height.size()) - 1;
        int i = 0;
        while (j > i) {
            temp = (j - i) * min(height[i], height[j]);
            area = max(area, temp);
            if (height[i] > height[j]) {
                j--;
            }
            else i++;
        }
        return area;
    }
};