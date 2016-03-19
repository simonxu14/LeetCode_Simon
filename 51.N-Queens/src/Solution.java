import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<Integer> temp = new ArrayList<Integer>();
        List<List<String>> result = new ArrayList<List<String>>();
        for (int i=0; i<n ; i++) {
        	temp.add(i+1);
        }
        backtrack_queen(temp, result, 0, n);
        return result;
    }
    
    public void backtrack_queen(List<Integer> temp, List<List<String>> result, int t, int n) {
    	if (t == n) {
    		List<String> pos = new ArrayList<String>();
    		for (int num : temp) {
    			StringBuilder sb = new StringBuilder();
    			for (int i = 0; i < n; i ++) {
    				if (i == num - 1) {
    					sb.append('Q');
    				} else {
    					sb.append('.');
    				}
    			}
    			pos.add(sb.toString());
    		}
    		result.add(pos);
    	} else {
    		for (int i=t; i<n; i ++) {
    			Collections.swap(temp, i, t);
    			if (legal(temp, t)) {
    				backtrack_queen(temp, result, t+1, n);
    			}
    			Collections.swap(temp, t, i);
    		}
    	}
    }
    
    public boolean legal(List<Integer> tmp,int t) {
        for(int i=0;i<t;i++){
            if(Math.abs(i-t) == Math.abs(tmp.get(i)-tmp.get(t))){
                return false;
            }
        }
        return true;
    }
    
}