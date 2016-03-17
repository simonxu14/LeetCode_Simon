import java.util.Arrays;

public class Solution {
    public int findDuplicate(int[] nums) {
        Arrays.sort(nums);
        int low = 0;
        int high = nums.length - 1;
        int mid = -1;
        while (low < high) {
        	mid = (high + low)/2;
        	if (mid > 0 && nums[mid] == nums[mid-1]) {
        		return nums[mid];
        	}
        	else if (mid + 1 < nums.length && nums[mid] == nums[mid+1]) {
        		return nums[mid];
        	}
        	else if (nums[mid] >= mid + 1) {
        		low = mid + 1;
        	}
        	else {
        		high = mid -1;
        	}
        }
        return 0;
    }
}