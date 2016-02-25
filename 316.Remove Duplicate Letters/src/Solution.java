import java.util.Stack;

public class Solution {
    public String removeDuplicateLetters(String s) {
    	if (s == null || s.length() == 0) {
    		return s;
    	}
    	int[] count = new int[26];
    	char[] res = new char[26];
    	int len = s.length();
    	for (int i=0; i<s.length(); i++) {
    		count[s.charAt(i) - 'a']++;
    	}
    	
    	int pos = 0;
    	for (int i = 0; i<len; i++) {
    		if (s.charAt(i) < s.charAt(pos)) {
    			pos = i;
    		}
    		count[s.charAt(i) - 'a']--;
    		if (count[s.charAt(i) - 'a'] == 0) {
    			break;
    		}
    	}
    	String charToRemove = String.valueOf(s.charAt(pos));
    	return charToRemove + removeDuplicateLetters(s.substring(pos+1).replaceAll(charToRemove,  ""));
    }
}