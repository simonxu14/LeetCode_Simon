//
//  Solution.cpp
//  116.Populating Next Right Pointers in Each Node
//
//  Created by Simon Xu on 9/8/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>
#include <queue>
#include <vector>
#include <math.h>

using namespace std;

struct TreeLinkNode {
    int val;
    TreeLinkNode *left, *right, *next;
    TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
};

class Solution {
public:
    void connect(TreeLinkNode *root) {
        queue<TreeLinkNode *> _queue;
        if (root == NULL) {
            return;
        }
        vector<TreeLinkNode*> list;
        _queue.push(root);
        list.push_back(root);
        while (!_queue.empty()) {
            if (_queue.front()->left != NULL) {
                _queue.push(_queue.front()->left);
                list.push_back(_queue.front()->left);
            }
            if (_queue.front()->right != NULL) {
                _queue.push(_queue.front()->right);
                list.push_back(_queue.front()->right);
            }
            _queue.pop();
        }
        int index = 0;
        int ss = 1;
        for (int i = 0; i < list.size(); i++) {
            if (i+1 == ss) {
                list[i]->next = NULL;
                index ++;
                ss = ss + pow(2, index);
            }
            else {
                list[i]->next = list[i+1];
            }
        }
        
        
    }
    
};