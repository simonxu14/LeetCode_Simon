public class Solution {
    public String convert(String s, int numRows) {
        if (s.length() == 0 || s.length() == 1) {
            return s;
        }
        if (s.length() <= numRows || numRows == 1) {
            return s;
        }
        StringBuilder sb = new StringBuilder();
        int step = 2 * (numRows - 1);
        
        for (int i = 0; i < numRows; i++) {
            int interval = step - 2*i;
            for (int j = i; j < s.length(); j += step) {
                sb.append(s.charAt(j));
                if (interval > 0 && interval < step && j + interval < s.length()) {
                    sb.append(s.charAt(j + interval));
                }
            }
        }
        return sb.toString();
    }
}