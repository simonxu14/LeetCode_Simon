/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
    	if (head == null || head.next == null || k == 0 || k == 1) {
    		return head;
    	}
    	ListNode node = head;
    	int sum_num = 0;
    	while (node != null) {
    		node = node.next;
    		sum_num ++;
    	}
    	if (sum_num < k) {
    		return head;
    	}
    	node = head;
    	ListNode head_pre = null;
    	int temp = 0;
    	while (node != null) {
    		int num = 0;
    		ListNode head_temp = node;
    		ListNode pre = null;
    		ListNode next = null;
    		if (sum_num >= k) {
    		    temp ++;
	    		while (num != k) {
	    			next = node.next;
	    			node.next = pre;
	    			pre = node;
	    			node = next;
	    			num ++;
	    			sum_num --;
	    		}
	    		if (head_pre != null) {
	    		    head_pre.next = pre;
	    		}
	    		head_temp.next = node;
	    		head_pre = head_temp;
	    		if (temp == 1) {
	    		    head = pre;
	    		}
    		} else {
    		    node = node.next;
    		}
    	}
    	return head;
    }
}