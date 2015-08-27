//
//  Solution.cpp
//  19.Remove Nth Node From End of List
//
//  Created by Simon Xu on 8/27/15.
//  Copyright (c) 2015 Simon Xu. All rights reserved.
//

#include <stdio.h>

//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head -> next == NULL && n == 1) {
            return NULL;
        }
        ListNode* index = head;
        ListNode* delete_Node_Pre = head;
        for (int m = n; m > 0; m--) {
            if (index -> next == NULL) {
                head = delete_Node_Pre -> next;
                return head;
            }
            index = index -> next;
        }
        while (index -> next != NULL) {
            index = index -> next;
            delete_Node_Pre = delete_Node_Pre -> next;
        }
        delete_Node_Pre -> next = delete_Node_Pre -> next -> next;
        return head;
    }
};