public class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    public void insert(String word) {
        TrieNode node = this.root;
        for (int i = 0; i < word.length(); i++) {
        	if (node.children.size() == 0) {
        		node.children.add(new TrieNode(word.charAt(i)));
    			node = node.children.get(0);
        	}
        	for (int j = 0; j < node.children.size(); j++) {
        		if (node.children.get(j).c == word.charAt(i)) {
        			node = node.children.get(j);
        			break;
        		}
        		else if (j == node.children.size()-1) {
        			node.children.add(new TrieNode(word.charAt(i)));
        			node = node.children.get(j+1);
        		}
        	}
        }
        node.word = true;
    }

    // Returns if the word is in the trie.
    public boolean search(String word) {
        TrieNode node = this.root;
        for (int i = 0; i < word.length(); i++) {
        	if (node.children.size() == 0)
    			return false;
        	for (int j = 0; j < node.children.size(); j++) {
        		if (node.children.get(j).c == word.charAt(i)) {
        			node = node.children.get(j);
        			break;
        		}
        		else if (j == node.children.size()-1) {
        			return false;
        		}
        	}
        }
        System.out.println(node.word);
        return node.word;
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    public boolean startsWith(String prefix) {
    	TrieNode node = this.root;
    	for (int i = 0; i < prefix.length(); i++) {
    		if (node.children.size() == 0)
    			return false;
    		for (int j = 0; j < node.children.size(); j++) {
    			if(node.children.get(j).c == prefix.charAt(i)) {
    				node = node.children.get(j);
        			break;
    			}
    			else if (j == node.children.size()-1) {
    				return false;
    			}
    		}
    	}
    	return true; 
    }
    
//    public static void main(String args[]) { 
//    	Trie trie = new Trie();
//    	trie.insert("ab");
//    } 
    
}



// Your Trie object will be instantiated and called as such:
// Trie trie = new Trie();
// trie.insert("somestring");
// trie.search("key");