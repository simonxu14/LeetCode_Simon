import java.util.ArrayList;
import java.util.List;

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
    public List<Integer> postorderTraversal(TreeNode root) {
    	List<Integer> result = new ArrayList<Integer>();
    	postorder(result, root);
    	return result;
        
    }
    
    public void postorder(List<Integer> result, TreeNode root) {
    	if (root == null) {
    		return;
    	}
    	postorder(result, root.left);
    	postorder(result, root.right);
    	result.add(root.val);
    }
}