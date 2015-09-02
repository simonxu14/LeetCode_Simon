//
//  Solution.cpp
//  122.Best Time to Buy and Sell Stock II
//
//  Created by Simon Xu on 9/1/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

//class Solution {
//public:
//    int maxProfit(vector<int>& prices) {
//        if (prices.size() == 0) {
//            return 0;
//        }
//        return greed(prices);
//    }
//    
//    int greed(vector<int>& sub) {
//        if (sub.size() == 0 || sub.size() == 1) {
//            return 0;
//        }
//        int min = INT_MAX;
//        int min_number = -1;
//        int max = INT_MIN;
//        int max_number = -1;
//        int m = 0;
//        int n;
//        bool index = true;
//        for (int k = 0; k < sub.size(); k++) {
//            if (sub[k] < sub [k+1]) {
//                index = false;
//                break;
//            }
//        }
//        if (index) {
//            return 0;
//        }
//        for (; m < sub.size(); m++) {
//            if (sub[m] > max) {
//                max = sub[m];
//                max_number = m;
//            }
//        }
//        if (max_number == 0) {
//            vector<int> right;
//            for (int k = 1; k < sub.size(); k++) {
//                right.push_back(sub[k]);
//            }
//            return greed(right);
//        }
//        for (n = 0; n < max_number; n++) {
//            if (sub[n] < min) {
//                min = sub[n];
//                min_number = n;
//            }
//        }
//        vector<int> left;
//        for (int i = 0; i < min_number; i ++) {
//            left.push_back(sub[i]);
//        }
//        vector<int> right;
//        for (int j = max_number + 1; j < sub.size(); j ++) {
//            right.push_back(sub[j]);
//        }
//        return sub[max_number] - sub[min_number] + greed(left) + greed(right);
//        
//    }
//};


class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() == 0 || prices.size() == 1) {
            return 0;
        }
        int i = 0;
        int sum = 0;
        while (i < prices.size() - 1) {
            int buy;
            int sell;
            while ((prices[i] >= prices[i+1]) && (i < prices.size() - 1)) {
                i++;
            }
            buy = i;
            while ((prices[i] <= prices[i+1]) && (i < prices.size() - 1)) {
                i++;
            }
            sell = i;
            sum = sum + prices[sell] - prices[buy];
        }
        return sum;
    }
};












