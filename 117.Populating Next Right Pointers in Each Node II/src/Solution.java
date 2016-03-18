import java.util.LinkedList;
import java.util.Queue;

/**
 * Definition for binary tree with next pointer.
 * public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void connect(TreeLinkNode root) {
    	if (root == null) {
    		return;
    	}
        Queue<TreeLinkNode> queue = new LinkedList<TreeLinkNode>();
        queue.add(root);
        int current_level_num = 1;
        int next_level_num = 0;
        while (!queue.isEmpty()) {
        	TreeLinkNode node = queue.poll();
        	current_level_num --;
        	
        	if (node.left != null) {
        		queue.add(node.left);
        		next_level_num ++;
        	}
        	if (node.right != null) {
        		queue.add(node.right);
        		next_level_num ++;
        	}
        	
        	if (current_level_num == 0) {
        		node.next = null;
        		current_level_num = next_level_num;
        		next_level_num = 0;
        	} else {
        		node.next = queue.peek();
        	}
        		
        }
    }
}