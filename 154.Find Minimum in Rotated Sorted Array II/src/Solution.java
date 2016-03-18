public class Solution {
    public int findMin(int[] nums) {
    	if (nums.length == 1) {
    		return nums[0];
    	}
        int low = 0;
        int high = nums.length - 1;
        int mid = -1;
        while (low < high) {
        	mid = (low + high)/2;
        	if (mid > 0 && nums[mid] < nums[mid-1]) {
        		return nums[mid];
        	}
        	else if (mid <= nums.length-1 && nums[mid] > nums[mid+1]) {
        		return nums[mid+1];
        	}
        	else if (nums[mid] <= nums[high]) {
        		high = mid-1;
        	}
        	else {
        		low = mid+1;
        	}
        }
        return Math.min(nums[low], nums[high]);
    }
}