class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.index=-1
        self.refs=0
    
    def addWord(self, word, i):
        curr=self
        curr.refs+=1
        for c in word:
            index=ord(c)-ord('a')
            if not curr.children[index]:
                curr.children[index]=TrieNode()
            curr=curr.children[index]
            curr.refs+=1
        curr.index=i

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for i in range(len(words)):
            root.addWord(words[i], i)
        rows, cols=len(board), len(board[0])
        res=[]
        
        def getIndex(c):
            index=ord(c)-ord('a')
            return index

        def dfs(r, c, node):
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c]=='*' or not node.children[getIndex(board[r][c])]:
                return 0
            tmp=board[r][c]
            board[r][c]='*'
            prev=node
            node=node.children[getIndex(tmp)]
            found=0
            if node.index!=-1:
                res.append(words[node.index])
                node.index=-1
                found+=1
            found+=dfs(r+1, c, node)
            found+=dfs(r-1, c, node)
            found+=dfs(r, c+1, node)
            found+=dfs(r, c-1, node)
            board[r][c]=tmp
            node.refs-=found
            if not node.refs:
                prev.children[getIndex(tmp)]=None
            return found
        
        for row in range(rows):
            for col in range(cols):
                root.refs-=dfs(row, col, root)
        return res