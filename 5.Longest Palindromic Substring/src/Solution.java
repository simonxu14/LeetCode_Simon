public class Solution {
    public String longestPalindrome(String s) {
        if (s.length() == 0)
            return s;
        if (s.length() == 1)
            return s;
        int max = 1;
        int start = 0;
        int end = 0;
        boolean[][] opt = new boolean[s.length()][s.length()];
        for (int i = 0; i < s.length(); i++) {
            for (int j = i; j >= 0; j --) {
                if (i == j) {
                    opt[j][i] = true;
                }
                else if (j == i - 1) {
                    if (s.charAt(i) == s.charAt(j)) {
                        opt[j][i] = true;
                        if ( (i-j+1) > max) {
                            max = i-j;
                            start = j;
                            end = i;
                        }
                    }
                    else {
                        opt[j][i] = false;
                    }
                }
                else {
                    if (s.charAt(i) == s.charAt(j) && opt[j+1][i-1]) {
                        opt[j][i] = true;
                        if ( (i-j+1) > max) {
                            max = i-j;
                            start = j;
                            end = i;
                        }
                    }
                    else {
                        opt[j][i] = false;
                    }
                }
                    
            }
        }
        return s.substring(start,end+1);
    }
}