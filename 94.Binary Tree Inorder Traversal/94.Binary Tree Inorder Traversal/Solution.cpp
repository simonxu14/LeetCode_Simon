//
//  Solution.cpp
//  94.Binary Tree Inorder Traversal
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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        if (root == NULL) {
            return result;
        }
        printNode(result, root);
        return result;
    }
    
    void printNode(vector<int> &result,TreeNode* root) {
        if (root->left != NULL) {
            printNode(result, root->left);
        }
        result.push_back(root->val);
        if (root->right != NULL) {
            printNode(result, root->right);
        }
    }
};