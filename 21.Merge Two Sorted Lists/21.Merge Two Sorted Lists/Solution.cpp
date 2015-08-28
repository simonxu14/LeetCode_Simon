//
//  Solution.cpp
//  21.Merge Two Sorted Lists
//
//  Created by Simon Xu on 8/28/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>
#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* result;
        ListNode* result_head;
        if (l1 == NULL && l2 ==NULL) {
            return NULL;
        }
        if (l1 == NULL) {
            return l2;
        }
        else if (l2 == NULL) {
            return l1;
        }
        if (l1->val < l2->val) {
            result = l1;
            result_head = result;
            l1 = l1->next;
        }
        else {
            result = l2;
            result_head = result;
            l2 = l2->next;
        }
        while (l1 != NULL && l2 != NULL) {
            if (l1->val < l2->val) {
                result->next = l1;
                result = result->next;
                l1 = l1->next;
            }
            else {
                result->next = l2;
                result = result->next;
                l2 = l2->next;
            }
        }
        if (l1 == NULL && l2 != NULL) {
            result->next = l2;
        }
        else if (l2 == NULL && l1 != NULL) {
            result->next = l1;
        }
        else {
            result ->next = NULL;
        }
        return result_head;
    }
};