/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    	String r = "abd";
    	r.indexOf(r.charAt(1));
        ListNode head = new ListNode(0);
        ListNode node = head;
        ListNode pre = new ListNode(0);
        int k = 0;
        while (l1 != null && l2 != null) {
            int temp = l1.val + l2.val + k;
            node.val = temp%10;
            k = temp/10;
            ListNode new_node = new ListNode(0);
            node.next = new_node;
            pre = node;
            node = new_node;
            l1 = l1.next;
            l2 = l2.next;
        }
        if (l1 == null && l2 == null) {
            if (k == 1) {
                node.val = 1;
                return head;
            }
            else {
                pre.next = null;
            }
        }
        if (l1 == null) {
            while (l2 != null) {
                int temp = k + l2.val;
                node.val = temp%10;
                k = temp/10;
                ListNode new_node = new ListNode(0);
                node.next = new_node;
                pre = node;
                node = new_node;
                l2 = l2.next;
            }
            if (k == 1) {
                node.val = 1;
                return head;
            }
            else {
                pre.next = null;
            }
        }
        if (l2 == null) {
            while (l1 != null) {
                int temp = k + l1.val;
                node.val = temp%10;
                k = temp/10;
                ListNode new_node = new ListNode(0);
                node.next = new_node;
                pre = node;
                node = new_node;
                l1 = l1.next;
            }
            if (k == 1) {
                node.val = 1;
                return head;
            }
            else {
                pre.next = null;
            }
        }
        return head;
    }
}