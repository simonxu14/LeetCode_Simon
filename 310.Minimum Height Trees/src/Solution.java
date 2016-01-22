import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (n <= 1) {
        	List<Integer> re = new ArrayList<Integer>();
        	re.add(0);
        	return re;
        }
        int degrees[] = new int[n];
        List<List<Integer>> graph = new ArrayList<List<Integer>>();
        for (int i = 0; i < n; i++) {
        	graph.add(new ArrayList<Integer>());
        }
        for (int i = 0; i < edges.length; i++) {
        	degrees[edges[i][0]] += 1;
        	degrees[edges[i][1]] += 1;
        	graph.get(edges[i][0]).add(edges[i][1]);
        	graph.get(edges[i][1]).add(edges[i][0]);
        }
        
        List<Integer> queue = new ArrayList<Integer>();
        List<Integer> ret = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
        	if (degrees[i] == 1)
        		queue.add(i);
        }
        while (!queue.isEmpty()) {
        	List<Integer> temp = new ArrayList<Integer>();
        	ret = queue;
        	for (int i = 0; i < queue.size(); i++) {
        		int x = queue.get(i);
        		List<Integer> edge = graph.get(x);
        		for (int j = 0; j < edge.size(); j++) {
        			degrees[edge.get(j)] -= 1;
        			if (degrees[edge.get(j)] == 1)
            			temp.add(edge.get(j));
        		}
        	}
        	queue = temp;
        }
    	return ret;
    }
}