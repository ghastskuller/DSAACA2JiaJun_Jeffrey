from stack import Stack
from binaryTree import BinaryTree

def buildParseTree(exp):
    tokens = exp.split()
    print(tokens)
    stack = Stack()
    tree = BinaryTree('?') #reference to the root node 
    stack.push(tree)
    currentTree = tree #reference to a node
    for t in tokens:
        # RULE 1: If token is '(' add a new node as left child
        # and descend into that node
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



while True:
    print("Please select your choice ('1','2','3'):")
    print("    1. Evaluate Expression")
    print("    2. Sort Expression")
    print("    3. Exit")
    userChoice = (input("Enter Choice: "))
    if userChoice.isnumeric()==False:
        print("Seems like what u entered is not a number. The choice u enter must be a number between 1-4!. Please try again!\n")
        input("Press Enter, to continue...")
    else:
        userChoice=int(userChoice)
        if userChoice is 1:
            expression  = ((input("Please enter the expression you want to evaluate: ")))
            ## the rest of the code
            input("Press any key, to continue...")
        elif userChoice is 2:
            inputFile = str(input("Please enter input file: "))
            outputFile = str(input("Please enter output: "))
            input("Press any key , to continue...")

        elif userChoice is 3:
            print("Bye, thanks for using ST1507 DSAA CA2 Assignment")
            quit()
        else:
            print("This number {} doesn't exist. Please make sure u type a number between 1-3. Try again!".format(userChoice))