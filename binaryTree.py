
## changing of evaluation modes and dept
f = open("config.txt", "r")
content = f.read()
content_list = content.splitlines()
f.close()
deptNode = content_list[0]
evaluationMode = content_list[1]
class BinaryTree:
    def __init__(self,key, leftTree = None, rightTree = None):
        self.key = key
        self.leftTree = leftTree
        self.rightTree = rightTree
    def setKey(self, key):
        self.key = key
    def getKey(self):
        return self.key
    def getLeftTree(self):
        return self.leftTree
    def getRightTree(self):
        return self.rightTree
    def insertLeft(self, key):
        if self.leftTree == None:
            self.leftTree = BinaryTree(key)
        else:
            t =BinaryTree(key)
            self.leftTree , t.leftTree = t, self.leftTree
    def insertRight(self, key):
        if self.rightTree == None:
            self.rightTree = BinaryTree(key)
        else:
            t =BinaryTree(key)
            self.rightTree , t.rightTree = t, self.rightTree
    def printPreorder(self, level):
        print( str(level*deptNode) + str(self.key))
        if self.leftTree != None:
            self.leftTree.printPreorder(level+1)
        if self.rightTree != None:
            self.rightTree.printPreorder(level+1) 
    def printInorder(self, level):
        if self.leftTree != None:
            self.leftTree.printInorder(level+1)
        print( str(level*deptNode) + str(self.key))
        if self.rightTree !=None:
            self.rightTree.printInorder(level+1)  