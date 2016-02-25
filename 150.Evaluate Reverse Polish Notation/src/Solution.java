import java.util.Stack;

public class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<Integer>();
        for (String ele : tokens) {
        	if (ele.equals("+") || ele.equals("-") || ele.equals("*") || ele.equals("/")) {
        		int num2 = stack.pop();
        		int num1 = stack.pop();
        		if (ele.equals("+"))
        			stack.push(num1+num2);
        		if (ele.equals("-"))
        			stack.push(num1-num2);
        		if (ele.equals("*"))
        			stack.push(num1*num2);
        		if (ele.equals("/"))
        			stack.push(num1/num2);
        	} else {
        		System.out.println(ele);
        		int num = Integer.parseInt(ele);
        		stack.push(num);
        	}
        }
        return stack.peek();
    }
}