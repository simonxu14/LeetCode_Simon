public class Solution {
    public int trap(int[] height) {
    	if (height.length <= 2) {
    		return 0;
    	}
    	int start = -1;
    	for (int i = 0; i < height.length; i++) {
    		if (height[i] > 0) {
    			start = i;
    			break;
    		}
    	}
    	if (start == -1) {
    		return 0;
    	}
    	int temp = start;
    	int end = 0;
    	int result = 0;
    	for (int i = temp+1; i < height.length; i++) {
    		if (i == height.length -1) {
    			if (height[height.length-1] >= height[start]) {
    				for (int k = start + 1; k < height.length-1; k++) {
        				if (height[k] < height[start]) {
        					result = result + (height[start] - height[k]);
        				}
        			}
    			} else {
    				int[] newList = new int[height.length-1 - start+1];
    				for (int m = 0; m <= height.length-1 - start; m++) {
    					newList[m] = height[height.length-1 - m];
//    					System.out.println(height[height.length-1 - m]);
    				}
    				result = result + trap(newList);
    			}
    		}
    		else if (height[i] >= height[start]) {
    			if (i - start > 1) {
    				for (int j = start+1; j < i; j++) {
    					result = result + (height[start] - height[j]);
    				}
    				start = i;
    			} else if ( i == start+1) {
    				start = i;
    			}
    		} 
    	}
    	return result;
    }
    
    public static void main(String[] args) {
		Solution S = new Solution();
		int[] list = {4,2,3};
		System.out.println(S.trap(list));
		
	}
}