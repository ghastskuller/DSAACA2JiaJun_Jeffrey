import re

class Stack:
    def __init__(self):
        self.__list= []
    def isEmpty(self):
        return self.__list == []
    def size(self):
        return len(self.__list)
    def clear(self):
        self.__list.clear()

    def push(self, item):
        self.__list.append(item)
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__list.pop()
    def get(self): 
        if self.isEmpty():
            return None
        else:
            return self.__list[-1]
    def __str__(self):
        output = '<'
        for i in range( len(self.__list) ):
            item = self.__list[i]
            if i < len(self.__list)-1 :
                output += f'{str(item)}, '
            else:
                output += f'{str(item)}'
                output += '>'
                return output

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
        print( str(level*'-') + str(self.key))
        if self.leftTree != None:
            self.leftTree.printPreorder(level+1)
        if self.rightTree != None:
            self.rightTree.printPreorder(level+1) 
    def printInorder(self, level):
        if self.leftTree != None:
            self.leftTree.printInorder(level+1)
        print( str(level*'-') + str(self.key))
        if self.rightTree !=None:
            self.rightTree.printInorder(level+1)    
def buildParseTree(exp):
    tokens.pop(0)
    tokens.pop(-1)
    stack = Stack()
    tree = BinaryTree('?') #reference to the root node 
    stack.push(tree)
    currentTree = tree #reference to a node
    for t in tokens:
        # RULE 1: If token is '(' add a new node as left child
        # and descend into that node
        if t == '':
            pass
        if t == '(':
            currentTree.insertLeft('?')
            stack.push(currentTree)
            currentTree = currentTree.getLeftTree() 
        # RULE 2: If token is operator set key of current node
        # to that operator and add a new node as right child
        # and descend into that node
        elif t in ['+', '-', '*', '/']:
            currentTree.setKey(t)
            currentTree.insertRight('?')
            stack.push(currentTree)
            currentTree = currentTree.getRightTree()
        # RULE 3: If token is number, set key of the current node
        # to that number and return to parent
        elif t not in ['+', '-', '*', '/', ')'] :
            currentTree.setKey(int(t))
            parent = stack.pop()
            currentTree = parent
        # RULE 4: If token is ')' go to parent of current node
        elif t == ')':
            currentTree = stack.pop()
        else:
            raise ValueError
    return tree

def evaluate(tree):
    leftTree = tree.getLeftTree()
    rightTree = tree.getRightTree()
    op = tree.getKey()
    if leftTree != None and rightTree != None:
        if op == '+':
            return evaluate(leftTree) + evaluate(rightTree)
        elif op == '-':
            return evaluate(leftTree) - evaluate(rightTree)
        elif op == '*':
            return evaluate(leftTree) * evaluate(rightTree)
        elif op == '/':
            return evaluate(leftTree) / evaluate(rightTree)
    else:
        return tree.getKey()


#exp = '( 2 + ( 4 * 5 ) )'
#tree = buildParseTree(exp)
#tree.printPreorder(0) 

# lab 2 
class BST(BinaryTree):
    def __init__(self,key,
        leftTree = None,
        rightTree = None):
            super().__init__(key,leftTree,rightTree) 
    def add(self, key):
        curNode = self
        while True:
            if key < curNode.key:
                if curNode.leftTree == None:
                    curNode.leftTree = BST(key)
                    break
                else:
                    curNode= curNode.leftTree
            elif key > curNode.key:
                if curNode.rightTree == None:
                    curNode.rightTree = BST(key)
                    break
                else:
                    curNode= curNode.rightTree        
    def __contains__(self,searchKey):
        curNode = self

        while True:
            if searchKey ==  curNode.getKey():
                return True
            # search left
            elif searchKey < curNode.getKey():
                if curNode.getLeftTree() == None:
                    return False
                else:
                    # traverse left
                    curNode = curNode.getLeftTree()
            # search right
            else: # >
                if curNode.getRightTree() == None:
                    return False
                else:
                    # traverse right
                    curNode = curNode.getRightTree()
# lab 3
class BST2(BinaryTree):
    def add(self,key):
        curNode = self
        while True:
            if key < curNode.getKey():
                if curNode.getLeftTree() == None or key > curNode.getLeftTree().getKey():
                    curNode.insertLeft(key)
                    break
                else:
                    curNode = curNode.getLeftTree()
            elif key> curNode.getKey():
                if curNode.getRightTree() == None or key < curNode.getRightTree().getKey():
                    curNode.insertRight(key)
                    break
                else:
                    curNode = curNode.getRightTree()

#tree = BST(55)
#tree.add(30)
#tree.add(73)
#tree.add(64)
#tree.add(89)
#tree.add(59)
#tree.add(70)
#tree.add(25)
#tree.add(71)
#tree.printPreorder(0)

# Main program
# import random
# items = [1,3,2,6,5,4,9,8,7]
# # Shuffle the items randomly
# random.shuffle(items)
# print('List shuffled as:', items, "\n")
# print('BST2 - Using squeeze in between add function')
# tree = BST2(items[0])
# for i in range(1,len(items)):
#     tree.add(items[i])
# tree.printPreorder(0)
# print()
# print('BST using add as leafs function')
# tree = BST(items[0])
# for i in range(1,len(items)):
#     tree.add(items[i])
# tree.printPreorder(0) 

exp = '(2+(4*5))'
tree = buildParseTree(exp)
tree.printInorder(0)
print (f'The expression: {exp} evaluates to: {evaluate(tree)}')