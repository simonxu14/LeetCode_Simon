import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
    	if (head == null) {
    		return null;
    	}
    	Map<RandomListNode, RandomListNode> map = new HashMap<>();
    	RandomListNode node = head;
        while (node != null) {
        	RandomListNode newNode = new RandomListNode(node.label);
        	map.put(node, newNode);
        	node = node.next;
        }
        node = head;
        while (node != null) {
        	if (node.random != null) {
        		map.get(node).random = map.get(node.random);
        	}
        	if (node.next != null) {
        		map.get(node).next = map.get(node.next);
        	}
        	node = node.next;
        }
        return map.get(head);
        
    }
}