import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public List<Integer> majorityElement(int[] nums) {
        List<Integer> list = new ArrayList<Integer>();
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        
        for (int i = 0; i < nums.length; i++) {
        	if (map.get(nums[i]) == null) {
        		map.put(nums[i], 1);
        	}
        	else {
        		map.put(nums[i], map.get(nums[i] + 1));
        	}
        }
        
        for (Integer in : map.keySet()) {
        	if (map.get(in) > nums.length/3)
        		list.add(in);
        }
        return list;
    }
}