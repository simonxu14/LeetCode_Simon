import java.util.HashMap;
import java.util.Map;

/**
 * Definition for undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     List<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */
public class Solution {
	Map<Integer, UndirectedGraphNode> nodes = new HashMap<Integer, UndirectedGraphNode>();
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        if (node == null)
        	return null;
        UndirectedGraphNode clone = null;
        if (!nodes.containsKey(node.label)) {
        	clone = new UndirectedGraphNode(node.label);
        	nodes.put(clone.label, clone);
        }
        else{
        	return nodes.get(node.label);
        }
        for (int i = 0; i < node.neighbors.size(); i++) {
        	if (node.neighbors.get(i).label == node.label) {
        		clone.neighbors.add(clone);
        	}
        	else{
        		clone.neighbors.add(cloneGraph(node.neighbors.get(i)));
        	}
        }
        return clone;
        
    }
}