import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<Integer> lexicalOrder(int n) {
        List<Integer> res = new ArrayList<Integer>();
        helper(0, n, res);
        return res;
    }
    
    private void helper(int pre, int n, List<Integer> res) {
    	for (int i = 0; i<=9; i++) {
    		int ele = 10*pre + i;
    		if (ele > n) break;
    		if (ele > 0) {
    			res.add(ele);
    			helper(ele, n, res);
    		}
    	}
    }
}