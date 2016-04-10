public class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        if (x == 0) {
            return true;
        }
        String str = String.valueOf(x);
        int left = 0;
        int right = str.length()-1;
        boolean result = true;
        while(left <= right) {
            if (str.charAt(left) != str.charAt(right)) {
                result = false;
                break;
            }
            left ++;
            right --;
        }
        return result;
    }
}