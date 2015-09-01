//
//  Solution.cpp
//  95.Unique Binary Search Trees II
//
//  Created by Simon Xu on 8/31/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<TreeNode*> generateTrees(int n) {
        vector<TreeNode*> result;
        if (n == 0) {
            result.push_back(NULL);
            return result;
        }
        result = generate(1, n);
        return result;
    }
    
    vector<TreeNode*> generate(int start, int end) {
        vector<TreeNode*> subTree;
        if (start > end) {
            subTree.push_back(NULL);
            return subTree;
        }
        for (int i = start; i <= end; i++) {
            vector<TreeNode*> leftSub = generate(start, i-1);
            vector<TreeNode*> rightSub = generate(i+1, end);
            for (int m = 0; m < leftSub.size(); m++) {
                for (int n = 0; n < rightSub.size(); n++) {
                    TreeNode *node = new TreeNode(i);
                    node->left = leftSub[m];
                    node->right = rightSub[n];
                    subTree.push_back(node);
                }
            }
        }
        return subTree;
        }
    
};