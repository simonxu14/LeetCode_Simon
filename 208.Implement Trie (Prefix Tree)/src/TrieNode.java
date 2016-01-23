import java.util.ArrayList;
import java.util.List;

class TrieNode {
    // Initialize your data structure here.
	char c;
	boolean word;
	List<TrieNode> children = new ArrayList<TrieNode>();
    public TrieNode() {}
    public TrieNode(char c) {
    	this.c = c;
    	this.word = false;
    }
}