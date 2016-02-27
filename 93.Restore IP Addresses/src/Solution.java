import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<String> restoreIpAddresses(String s) {
    	List<Integer> current = new ArrayList<Integer>();
        List<List<Integer>> result = new ArrayList<List<Integer>>();
//        System.out.println(result);
        List<String> res = new ArrayList<String>();
    	if (s.length() > 12)
    		return res;
    	recursive(s, current, result);
        for (List<Integer> list:result) {
        	StringBuilder sb = new StringBuilder();
        	for (Integer ele:list) {
        		sb.append(ele.toString());
        		sb.append(".");
        	}
        	res.add(sb.subSequence(0, sb.length()-1).toString());
        }
        return res;
    }
    
    public void recursive(String s, List<Integer> current, List<List<Integer>> result) {
    	if (s.length() > 0 && s.charAt(0) == '0') {
    		current.add(Integer.parseInt(s.substring(0, 1)));
    		recursive(s.substring(1, s.length()), current, result);
    		current.remove(current.size()-1);
    		return;
    	}
//    	if (current.size() >= 4 && s.length() != 0)
//			return;
//    	if (current.size() == 3) {
//    		if (s.length() == 0)
//    	        return;
//    		if (s.length()>3)
//    			return;
//    		if (Integer.parseInt(s) > 255)
//    			return;
//    	}
    	if (s.length() == 0) {
    		if (current.size() == 4) {		
//    			List<Integer> temp = new ArrayList<Integer>();
//    			for (int i:current)
//    				temp.add(i);
//    			result.add(temp);
    			List<Integer> temp = new ArrayList<Integer>(current);
    			result.add(temp);
    		}
    		return;
    	}
    	else if (s.length() == 1) {
    		if (current.size() == 3) {
    			List<Integer> temp = new ArrayList<Integer>(current);
    			temp.add(Integer.parseInt(s));
    			result.add(temp);
    		}
    		return;
    	}
    	else if (s.length() == 2) {
    		if (current.size() == 3) {
    			List<Integer> temp = new ArrayList<Integer>(current);
    			temp.add(Integer.parseInt(s));
    			result.add(temp);
    		}
    		if (current.size() == 2) {
    			List<Integer> temp = new ArrayList<Integer>(current);
    			temp.add(Integer.parseInt(s.substring(0,1)));
    			temp.add(Integer.parseInt(s.substring(1,2)));
    			result.add(temp);
    		}
    		return;
    	}
    	else {
    		current.add(Integer.parseInt(s.substring(0, 1)));
    		recursive(s.substring(1, s.length()), current, result);
    		current.remove(current.size()-1);
    		
    		current.add(Integer.parseInt(s.substring(0, 2)));
    		recursive(s.substring(2, s.length()), current, result);
    		current.remove(current.size()-1);
    		
    		if (Integer.parseInt(s.substring(0, 3))<=255) {
    			
    			current.add(Integer.parseInt(s.substring(0, 3)));
        		recursive(s.substring(3, s.length()), current, result);
        		current.remove(current.size()-1);
    		}
    		return;
    	}
    }
    
    public static void main(String[] args) {
    	Solution s = new Solution();
    	System.out.println(s.restoreIpAddresses("255255255255"));
	}
}