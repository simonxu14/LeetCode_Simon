//
//  Solution.cpp
//  226.Invert Binary Tree
//
//  Created by Simon Xu on 9/22/15.
//  Copyright © 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>
#include <iostream>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
 
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        int index = 0;
        if (root == NULL) {
            return NULL;
        }
        if (root -> left != NULL && root -> right != NULL) {
            invertTree(root -> left);
            invertTree(root -> right);
            TreeNode* node;
            node = root -> left;
            root -> left = root -> right;
            root -> right = node;

        }
        if (root -> left == NULL && root ->right == NULL) {
            return root;
        }
        if (root -> left == NULL) {
            invertTree(root -> right);
            root -> left = root -> right;
            root -> right = NULL;
        }
        if (root -> right == NULL) {
            invertTree(root -> left);
            root -> right = root -> left;
            root -> left = NULL;
        }
        return root;
    }
};