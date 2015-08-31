//
//  Solution.cpp
//  24.Swap Nodes in Pairs
//
//  Created by Simon Xu on 8/30/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
 };

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (head == NULL || head->next == NULL) {
            return head;
        }
        ListNode* proNode = head;
        ListNode* nextNode = head->next;
        while (proNode != NULL && nextNode != NULL) {
            swap(& proNode->val, & nextNode->val);
            if (nextNode->next == NULL) {
                break;
            }
            if (nextNode->next->next == NULL) {
                break;
            }
            proNode = proNode->next;
            proNode = proNode->next;
            nextNode = nextNode->next;
            nextNode = nextNode->next;
        }
        return head;
    }
    
    void swap(int* a, int* b) {
        int index;
        index = *a;
        *a = *b;
        *b = index;
    }
};