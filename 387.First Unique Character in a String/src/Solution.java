import java.util.HashMap;

public class Solution {
    public int firstUniqChar(String s) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i=0; i<s.length(); i++) {
        	if (map.get(s.charAt(i) - 'a') != null) {
        		map.put(s.charAt(i) - 'a', -1);
        	}
        	else {
        		map.put(s.charAt(i) - 'a', 1);
        	}
        }
        for (int i=0; i<map.size(); i++) {
        	if (map.get(i) == 1)
        		return i;
        }
    	return -1;
    }
}