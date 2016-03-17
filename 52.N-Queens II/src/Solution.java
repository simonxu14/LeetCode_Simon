import java.util.ArrayList;
import java.util.List;

public class Solution {
	int count = 0;
	
	public int totalNQueens(int n) {
		List<Integer> current = new ArrayList<Integer>();
		DFS(count, current, 0, n);
		return count;
	}
	
	private void DFS(int count, List<Integer> current, int pos, int n) {
		if (pos == n) {
			System.out.println("AAA");
			count ++;
		}
		else {
			for (int i = 0; i < n; i++) {
				current.add(i);
				if (check(current)) {
					DFS(count, current, pos+1, n);
				}
				current.remove(current.size()-1);
			}
		}
	}
	
	private boolean check(List<Integer> current) {
		int size = current.size();
		int loc = current.get(size-1);
		for (int i = 0; i < size-1; i++) {
			if (current.get(i) == loc) {
				return false;
			}
			if (Math.abs(current.get(i)-loc) == Math.abs(i-size+1)) {
				return false;
			}
		}
		return true;
	}
	
	public static void main(String[] args) {
		Solution S = new Solution();
		System.out.println(S.totalNQueens(1));
	}
}
