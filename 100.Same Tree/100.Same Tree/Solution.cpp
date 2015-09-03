//
//  Solution.cpp
//  100.Same Tree
//
//  Created by Simon Xu on 9/3/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
 
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p && !q) {
            return true;
        }
        if (!p || !q) {
            return false;
        }
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right) && (p->val == q->val);
    }
};