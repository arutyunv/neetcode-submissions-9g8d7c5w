# You need to define class TreeNode first 
class TrieNode:
    def __init__(self):
        self.children = {} # char -> TrieNode
        self.isEnd = False # marks end of word


class PrefixTree:
    def __init__(self):
        # “When I create a PrefixTree, I also create the first empty node”
        self.root = TrieNode() # create the root node here
        
    def insert(self, word):
        # Start from the root node (beginning of the Trie)
        node = self.root  
        
        # Go through each character in the word one by one
        for char in word:
            # If there is NO path for this character yet...
            if char not in node.children:
                # then create a new node for this character and store it
                node.children[char] = TrieNode()
            
            # Move the pointer to the next node (go deeper into the tree)
            node = node.children[char]
            
        # After processing all characters, mark this node as the END of a word
        node.isEnd = True
   

    def search(self, word):
        # Start from the root of the Trie
        node = self.root  
        
        # Go through each character in the word
        for char in word:
            # If the current character path does NOT exist in the Trie...
            if char not in node.children:
                # then the word is definitely not in the Trie
                return False

            # Move to the next node (follow the path of the character)
            node = node.children[char]
            
        # After checking all characters:
        # return True ONLY if this node marks the end of a word
        return node.isEnd
    
        
    def startsWith(self, prefix):
        # Start from the root
        node = self.root  

        # Go through each character in the prefix
        for char in prefix:
            
            # If at any point the path doesn't exist
            if char not in node.children:
                # then no word has this prefix
                return False
            
            # Move deeper into the Trie
            node = node.children[char]
            
        # If we successfully followed the whole prefix,
        # then at least one word starts with it
        return True
    
        
        