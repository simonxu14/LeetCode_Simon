/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int countNodes(TreeNode root) {
        int h = height(root);
        int nodes = 0;
        while (root != null) {
        	if (height(root.right) == h-1) {
        		nodes += Math.pow(2, h);
        		root = root.right;
        	}
        	else {
        		nodes += Math.pow(2, h-1);
        		root = root.left;
        	}
        	h--;
        }
        return nodes;
    }
    
    public int height(TreeNode root) {
    	if (root == null)
    		return -1;
    	else
    		return height(root.left) + 1;
    }
    
}