public class Solution {
    public int calculate(String s) {
    	s = s + "+";
//    	System.out.println(s);
    	String number = "";
    	int temp = 0;
    	String operation = "+";
    	int result = 0;
    	
        for(int i=0; i<s.length(); i++ ) {
        	if(s.charAt(i) == ' ')
        		continue;
        	else if(Character.isDigit(s.charAt(i))) {
        		number += s.charAt(i);
        	}
        	else {
        		if(operation.equals("+")) {
        			result += temp;
        			temp = Integer.valueOf(number);
        		}
        		else if(operation.equals("-")) {
        			result += temp;
        			temp = (-1)*Integer.valueOf(number);
        		}
        		else if(operation.equals("*")) {
        			temp *= Integer.valueOf(number);
        		}
        		else if(operation.equals("/")) {
        			temp /= Integer.valueOf(number);
        		}
        		number = "";
        		operation = String.valueOf(s.charAt(i));
        	}
        }
        return result + temp;
    }
    
//    public static void main(String[] args) {
//		Solution S = new Solution();
//		System.out.println(S.calculate("1"));
//	}
}