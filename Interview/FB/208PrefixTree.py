import collections
class TrieNode(object):
        # Initialize your data structure here.
    def __init__(self):
        self.word = False
        self.children = {}

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i]=TrieNode()
            node = node.children[i]
        print node.children
        node.word=True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node=self.root
        for i in word:
            if i not in node.children:
                return False
            node=node.children[i]
        return node.word

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        node=self.root
        for i in prefix:
            if i not in node.children:
                return False
            node=node.children[i]
        return True


    # Your Trie object will be instantiated and called as such:
    # trie = Trie()
    # trie.insert("somestring")
    # trie.search("key")

Trie().insert('abc')
Trie().insert('aba')
Trie().insert('tea')
Trie().insert('bad')
print Trie().search('abc')