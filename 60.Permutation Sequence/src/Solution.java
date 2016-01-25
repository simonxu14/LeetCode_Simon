public class Solution {
    public String getPermutation(int n, int k) {
        String ll = "";
    	for (int i = 1; i < n+1; i++) {
        	ll += Integer.toString(i);
        }
    	int divisor = 1;
    	for (int i = 1; i < n; i++) {
    		divisor *= i;
    	}
    	String answer = "";
    	
    	int group_num = 0;
    	char choose;
    	String ll2 = "";
    	while (k > 0 && k <= divisor*n) {
    		group_num = k / divisor;
    		k %= divisor;
    		
    		if (k > 0) {
    			choose = ll.charAt(group_num);
    			ll = ll.substring(0, group_num) + ll.substring(group_num+1);
    			answer += choose;
    		}
    		else {
    			choose = ll.charAt(group_num - 1);
    			ll = ll.substring(0, group_num-1) + ll.substring(group_num);
    			answer += choose;
    			StringBuffer sb=new StringBuffer(ll);
    			sb.reverse();
    			ll2 = sb.toString();
    			answer = answer + ll2;
    			break;
    		}
    		divisor /= ll.length();
    	}
    	return answer;
    }
}