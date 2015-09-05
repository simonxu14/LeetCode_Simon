//
//  Solution.cpp
//  98.Validate Binary Search Tree
//
//  Created by Simon Xu on 9/5/15.
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
    bool isValidBST(TreeNode* root) {
        if (root == NULL) {
            return true;
        }
        if (root -> left == NULL && root -> right == NULL) {
            return true;
        }
        vector<int> result;
        print(root, result);
        bool re = true;
        for (int i; i < result.size()-1; i++) {
            if (result[i] >= result[i+1]) {
                re = false;
                break;
            }
        }
        return re;
    }
    
    void print(TreeNode* node, vector<int> & DFS) {
//        if (node->left == NULL && node -> right == NULL) {
//            return true;
//        }
//        node->val > left_max
//        node->val < right_min
//        else if (node -> left == NULL && node -> right != NULL) {
//            return (node->val < node->right->val && node->val <  && ifBST(node->right));
//        }
//        return (node->val > node->left->val) && (node->val < node->right->val) && (node->val > node->left->right->val) && (node->val < node->right->left->val) && isBST(node->left) && isBST(node->right);
        if (node->left != NULL) {
            print(node->left, DFS);
        }
        DFS.push_back(node->val);
        if (node->right != NULL) {
            print(node->right, DFS);
        }
    }
};