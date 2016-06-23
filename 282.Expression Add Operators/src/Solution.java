import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<String> addOperators(String num, int target) {
        List<String> result = new ArrayList<String>();
        dfs(num.toCharArray(), result, "", 0, target, 0);
        return result;
    }
    
    public void dfs(char[] nums, List<String> res, String str, int pos, long rem, long prevNum) {
    	if (rem == prevNum && pos == nums.length) {
    		res.add(str);
    		return;
    	}
    	long val = 0;
    	for (int i=pos; i<nums.length;i++) {
    		val = val*10 + (nums[i]-'0');
    		if (i>pos && nums[pos]=='0') break;
    		if (pos==0) dfs(nums, res, ""+val, i+1, rem, val);
    		else {
    			dfs(nums, res, str+"+"+val, i+1, rem-prevNum, val);
    			dfs(nums, res, str+"-"+val, i+1, rem-prevNum, -val);
    			dfs(nums, res, str+"*"+val, i+1, rem, prevNum*val);
    		}
    	}
    }
}