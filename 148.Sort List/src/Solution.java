/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null) {
        	return head;
        }
        ListNode p = head;
        int i = 0;
        while (p != null) {
        	i += 1;
        	p = p.next;
        }
        return mergeSort(head, i);
    }
    
    public ListNode mergeSort(ListNode head, int k) {
    	if (k == 1) {
    		return head;
    	}
//    	if (k == 2) {
//    		System.out.println(head.val);
//    		if (head.val >= head.next.val)
//    			return head;
//    		else {
//    			head.next.next = head;
//    			head = head.next;
//    			head.next.next = null;
//    			return head;
//    		}
//    	}
    	
    	ListNode mid = head;
    	for (int i = 0; i < k/2 - 1; i++)
    		mid = mid.next;
    	ListNode tmp = mid;
    	mid = mid.next;
    	tmp.next = null;
//    	System.out.println(mid.val);
    	ListNode left_head = mergeSort(head, k/2);
    	ListNode right_head = mergeSort(mid, k - k/2);
    	return merge(left_head, right_head);
    }
    
    public ListNode merge(ListNode h1, ListNode h2) {
    	ListNode dummy = new ListNode(0);
    	ListNode p = dummy;
    	while (h1 != null && h2 != null) {
    		if (h1.val <= h2.val) {
    			p.next = h1;
    			p = p.next;
    			h1 = h1.next;
    		}
    		else {
    			p.next = h2;
    			p = p.next;
    			h2 = h2.next;
    		}
    	}
    	if (h1 == null && h2 != null)
    		p.next = h2;
    	else if (h2 == null && h1 != null)
    		p.next = h1;
    	return dummy.next;
    }
	
	
	
	
	
//	public ListNode sortList(ListNode head) {
//		if (head == null || head.next == null)
//			return head;
//		ListNode fast = head;
//		ListNode slow = head;
//		ListNode prev = head;
//		
//		while (fast != null && fast.next != null) {
//			prev = slow;
//			slow = slow.next;
//			fast = fast.next.next;
//		}
//		ListNode second = prev.next;
//		prev.next = null;
//		ListNode first = sortList(head);
//		second = sortList(second);
//		head = mergeList(first, second);
//		return head;
//	}
//	
//	private ListNode mergeList(ListNode first, ListNode second) {
//		ListNode dummy = new ListNode(0);
//		ListNode merged = dummy;
//		while(first != null && second != null) {
//			if (first.val <= second.val) {
//				merged.next = first;
//				merged = merged.next;
//				first = first.next;
//			}
//			else {
//				merged.next = second;
//				merged = merged.next;
//				second = second.next;
//			}
//		}
//		if (first != null || second != null)
//			merged.next = (first != null)? first : second;
//		return dummy.next;
//	}
}