public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int max = 0;
        String current = "";
        for (int i = 0; i < s.length(); i++) {
            if (current.indexOf(s.charAt(i)) == -1) {
                current = current + s.charAt(i);
            } else {
                current = current.substring(current.indexOf(s.charAt(i))+1, current.length());
                current = current + s.charAt(i);
            }
            if (current.length() > max) {
                max = current.length();
            }
            
        }
        return max;
    }
}