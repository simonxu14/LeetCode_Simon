import java.awt.print.Printable;
import java.util.Stack;

public class Solution {
    public int lengthLongestPath(String input) {
        int ret = 0;
        String[] paths = null;
        paths = input.split("\n");
        for (String path:paths)
        	System.out.println(path);
        Stack<Integer> st = new Stack<Integer>();
        st.push(0);
        for (String path:paths) {
        	String[] tmp = path.split("\t");
        	String last = tmp[tmp.length - 1];
        	while (st.size() > tmp.length) 
        		st.pop();
        	st.push(st.peek() + last.length() + 1);
        	if (last.indexOf(".") != -1)
        		ret = Math.max(ret, st.peek()-1);
        }
        return ret;
    }
    
    public static void main(String[] args) {
		String example = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext";
		Solution solution = new Solution();
		System.out.println(solution.lengthLongestPath(example));
	}
}

