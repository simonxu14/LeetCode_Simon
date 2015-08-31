//
//  Solution.cpp
//  23.Merge k Sorted Lists
//
//  Created by Simon Xu on 8/30/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        vector<int> number;
        ListNode* result = (ListNode *)malloc(sizeof(ListNode));
        ListNode* result_head = NULL;
        if (lists.size() == 0) {
            return result_head;
        }
        ListNode* node;
        for (int k = 0; k < lists.size(); k++) {
            node = lists[k];
            while (node != NULL) {
                number.push_back(node->val);
                node = node->next;
            }
        }
        if (number.size() == 0) {
            return result_head;
        }
        sort(number.begin(), number.end());
        result->val = number[0];
        result->next = NULL;
        result_head = result;
        for (int m = 1; m < number.size(); m++) {
            insertNode(result, number[m]);
            result = result->next;
        }
        return result_head;
    }
    
    void insertNode(ListNode* result, int n) {
        ListNode* current = (ListNode *)malloc(sizeof(ListNode));
        current->val = n;
        current->next = NULL;
        result->next = current;
    }
};

