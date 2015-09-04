//
//  Solution.cpp
//  102.Binary Tree Level Order Traversal
//
//  Created by Simon Xu on 9/4/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <queue>
#include <vector>
#include <math.h>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };
 
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        queue<TreeNode *> S;
        vector<int> current;
        vector<vector<int>> result;
        if (root == NULL) {
            return result;
        }
        S.push(root);
        int layer = 1;
        int next_layer = 0;
        int i = 0;
        while (!S.empty()) {
            current.push_back(S.front()->val);
            if (S.front()->left != NULL) {
                S.push(S.front()->left);
                next_layer++;
            }
            if (S.front()->right != NULL) {
                S.push(S.front()->right);
                next_layer++;
            }
            S.pop();
            i++;
            if (layer == i) {
                result.push_back(current);
                current.clear();
                layer = next_layer;
                next_layer = 0;
                i = 0;
            }
        }
        return result;
    }
};