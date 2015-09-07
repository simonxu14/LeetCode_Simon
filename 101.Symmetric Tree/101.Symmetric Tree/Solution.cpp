//
//  Solution.cpp
//  101.Symmetric Tree
//
//  Created by Simon Xu on 9/7/15.
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

//class Solution {
//public:
//    bool isSymmetric(TreeNode* root) {
//        if ((root == NULL) || (root->left == NULL && root->right == NULL) ) {
//            return true;
//        }
//        queue<TreeNode*> _queue;
//        _queue.push(root);
//        vector<int> _vector;
//        _vector.push_back(root->val);
//        while (!_queue.empty()) {
//            if (_queue.front()->left == NULL) {
//                _vector.push_back(-1);
//            }
//            else {
//                _queue.push(_queue.front()->left);
//                _vector.push_back(_queue.front()->left->val);
//            }
//            if (_queue.front()->right == NULL) {
//                _vector.push_back(-1);
//            }
//            else {
//                _queue.push(_queue.front()->right);
//                _vector.push_back(_queue.front()->right->val);
//            }
//            _queue.pop();
//        }
//        int index = 1;
//        for (int i = 1; ; i++) {
//            for (int j = index; j < index + pow(2, i)/2; j++) {
//                if (_vector[j] != _vector[2*index + pow(2, i)-j-1]) {
//                    return false;
//                }
//            }
//            index = index + pow(2, i);
//            if (index >= _vector.size()) {
//                break;
//            }
//        }
//        
//        return true;
//    }
//};


class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (root == NULL) {
            return true;
        }
        return isSym(root->left, root->right);
    }
    
    bool isSym(TreeNode* left, TreeNode* right) {
        if (left == NULL && right == NULL) {
            return true;
        }
        if (left == NULL && right != NULL) {
            return false;
        }
        if (left != NULL && right == NULL) {
            return false;
        }
        if (left->val != right->val) {
            return false;
        }
        if (!isSym(left->left, right->right)) {
            return false;
        }
        if (!isSym(left->right, right->left)) {
            return false;
        }
        return true;
    }
};






