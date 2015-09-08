//
//  Solution.cpp
//  104.Maximum Depth of Binary Tree
//
//  Created by Simon Xu on 9/8/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
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

//class Solution {
//public:
//    int maxDepth(TreeNode* root) {
//        if (root == NULL) {
//            return 0;
//        }
//        int* layer;
//        *layer = 0;
//        int* result;
//        *result = 0;
//        DFS(root, layer, result);
//        return *result;
//    }
//    
//    void DFS(TreeNode* node, int* layer, int* result) {
//        if (node->left == NULL && node->right == NULL) {
//            layer += 1;
//        }
//        if (node->left != NULL && node->right == NULL) {
//            return DFS(node->left, layer);
//            
//        }
//        if (node->left == NULL && node->left == NULL) {
//            return DFS(node->left, layer);
//        }
//        DFS(node->left, layer);
//        DFS(node->right, layer);
//    }
//};


class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == NULL) {
            return 0;
        }
        int lmax = maxDepth(root->left);
        int rmax = maxDepth(root->right);
        return max(lmax, rmax)+1;
    }
};












