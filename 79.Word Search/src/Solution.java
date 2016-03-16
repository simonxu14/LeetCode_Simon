import java.util.ArrayList;
import java.util.List;

public class Solution {
    public boolean exist(char[][] board, String word) {
    	if (word.length() == 0)
    		return true;
    	List<Integer> first_list = new ArrayList<Integer>();
        for (int i = 0; i < board.length; i++) {
        	for (int j = 0; j < board[0].length; j++) {
        		if (board[i][j] == word.charAt(0)) {
        			first_list.add(i);
        			first_list.add(j);
        		}
        	}
        }
        if (first_list.size() == 0)
        	return false;
        if (word.length() == 1)
        	return true;
        for (int k = 0; k < first_list.size(); k = k+2) {
        	char c = board[first_list.get(k)][first_list.get(k+1)];
    		board[first_list.get(k)][first_list.get(k+1)] = '0';
        	if (dfs(board, first_list.get(k)+1, first_list.get(k+1), word.substring(1)) == true)
        		return true;
        	else if (dfs(board, first_list.get(k)-1, first_list.get(k+1), word.substring(1)) == true)
        		return true;
        	else if (dfs(board, first_list.get(k), first_list.get(k+1)+1, word.substring(1)) == true)
        		return true;
        	else if (dfs(board, first_list.get(k), first_list.get(k+1)-1, word.substring(1)) == true)
        		return true;
        	else
        		board[first_list.get(k)][first_list.get(k+1)] = c;
        }
        return false;
    }
    
    public boolean dfs(char[][] board, int i, int j, String word) {
    	if (i<0 || i>=board.length || j<0 || j>= board[0].length) {
    		return false;
    	}
    	if (board[i][j] != word.indexOf(0))
    		return false;
    	if (word.length() == 1)
    		return true;
    	else {
    		char temp = board[i][j];
    		board[i][j] = '0';
    		if (dfs(board, i+1, j, word.substring(1)) == true)
    			return true;
    		else if (dfs(board, i-1, j, word.substring(1)) == true)
    			return true;
    		else if (dfs(board, i, j+1, word.substring(1)) == true)
    			return true;
    		else if (dfs(board, i, j-1, word.substring(1)) == true)
    			return true;
    		else{
    			board[i][j] = temp;
    			return false;
    		}	
    	}
    }
    
}