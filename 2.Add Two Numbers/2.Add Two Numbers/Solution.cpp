//
//  Solution.cpp
//  2.Add Two Numbers
//
//  Created by Simon Xu on 8/13/15.
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
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        return addNote(l1, l2, 0);
    }
    ListNode *addNote(ListNode *l1, ListNode *l2, int carry){
        if (!l1 && !l2 && carry == 0) {
            return NULL;
        }
        int a = 0, b = 0;
        if(l1)  a = l1 -> val;
        if(l2)  b = l2 -> val;
        int value = a + b + carry;
        ListNode *head = new ListNode(value % 10);
        head -> next = addNote(l1? l1->next: NULL, l2? l2->next: NULL, value / 10);
        return head;
    }
};