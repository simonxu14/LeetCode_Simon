import java.util.Stack;

public class Solution {
	public int longestValidParentheses(String s) {
		Stack<Integer> stack = new Stack<Integer>();
		int left = -1;
		int max = 0;
		for (int i = 0; i < s.length(); i++) {
			if (s.charAt(i) == '(') {
				stack.push(i);
			}
			else {
				if (stack.isEmpty()) {
					left = i;
				}
				else {
					stack.pop();
					if(stack.isEmpty()) {
						max = Math.max(max, i-left);
					}
					else {
						max = Math.max(max, i-stack.peek());
					}
				}
			}
		}
		return max;
	}
}