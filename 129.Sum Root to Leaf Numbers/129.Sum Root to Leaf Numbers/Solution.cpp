^{
    <#code#>
}//
//  Solution.cpp
//  129.Sum Root to Leaf Numbers
//
//  Created by Simon Xu on 9/7/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int sumNumbers(TreeNode* root) {
        if (root == NULL) {
            return 0;
        }
        vector<int> result;
        string current_str;
        int sum = 0;
        if (root->val == 0 && root->left == NULL && root->right ==NULL) {
//            if (root->left == NULL && root->right == NULL) {
//                return 0;
//            }
//            if (root->left == NULL && root->right != NULL) {
//                DFS(root->right, current_str, result);
//            }
//            if (root->right == NULL && root->left != NULL) {
//                DFS(root->left, current_str, result);
//            }
//            else {
//                DFS(root->left,current_str, result);
//                for (int i = 0; i<result.size(); i++) {
//                    sum += result[i];
//                }
//                current_str = "";
//                result.clear();
//                DFS(root->right, current_str, result);
//                for (int i = 0; i<result.size(); i++) {
//                    sum += result[i];
//                }
//                return sum;
//            }
            return 0;
        }
        else DFS(root, current_str, result);
        
        for (int i = 0; i<result.size(); i++) {
            sum += result[i];
        }
        return sum;
    }
    
    void DFS(TreeNode* node, string current_str, vector<int>& result) {
        current_str = current_str + to_string(node->val);
        if (current_str[0] == 0) {
            current_str = "";
        }
        if (node->left == NULL && node->right == NULL) {
            result.push_back(atoi(current_str.c_str()));
            return;
        }
        if (node->left == NULL && node->right != NULL) {
            DFS(node->right, current_str, result);
            return;
        }
        if (node->left != NULL && node->right == NULL) {
            DFS(node->left, current_str, result);
            return;
        }
        DFS(node->left, current_str, result);
        DFS(node->right, current_str, result);
    }
    
};