import java.util.HashMap;
import java.util.Map;

public class Solution {
	public int[] twoSum(int[] nums, int target) {
//		int[] result = new int[2];
//		for (int i = 0; i < nums.length; i++) {
//			for (int j = i+1; j < nums.length; j++) {
//				if (nums[i] + nums[j] == target) {
//					result[0] = i;
//					result[1] = j;
//				}
//			}
//		}
//		return result;

		int[] result = {0,0};
		Map<Integer, Integer> map = new HashMap<>();
		for (int i = 0; i < nums.length; i++) {
			if (map.containsKey(target - nums[i])) {
				result[0] = map.get(target - nums[i]);
				result[1] = i;
				return result;
			}
			else {
				map.put(nums[i], i);
			}
			
		}
		return result;
	}	
}
