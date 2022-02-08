from stack import Stack
from binaryTree import BinaryTree
from binaryTree import evaluationMode
def tokenising(expression):
    
    tokens = []
    
    i = 0
    
    while(i< len(expression)):
        ## this means expression[i] is confirm an operator
        if expression[i] is '(' or ')' or '+' or '/':
            ## appending expression[i] to tokens
            tokens.append(expression[i])
            i=i+1
        elif expression[i] is '*':
            print(tokens)
            ## check if it's a power (**)
            if expression[i+1] is '*':
                ## this means its a power operator
                tokens.append('**')
                print(tokens)
                i=i+2
            else:
                ## this means its just a simple * operator
                tokens.append(expression[i])
                i=i+1
        elif expression[i] is '-':
            ##check if the character before is another operator or open bracket
            if expression[i-1] is '(' or ')' or '-' or '*' or '/':
                ## this means the '-' is a negative sign
                ## we need another loop to extract out all the digits after the negative sign
                j = i +1
                num = expression[i]

                ## this loop accounts for decimal points too
                while ((expression[j] is int) or (expression[j] is '.')):
                    num.concat(expression[j])
                    j=j+1
                ## once code reaches here, we have num as the fully tokenised negative number
                tokens.append(num)
                i=j
            else:
                ## this means the '-' is a minus sign
                tokens.append(expression[i])
                
                i=i+1
        elif expression[j] is int :
            # we need another loop to extract out all the digits after the digit (if any)
            j = i+1 
            num = expression[i]

            ## this loop accounts for decimal points too
            while ((expression[j] is int )or (expression[j] is '.')):
                num.concat(expression[j])
                j=j+1
            
            tokens.append(num)
            i=j
        else:
            tokens.append(expression[i])
            i=i+1
            
    return tokens
def buildParseTree(exp):
    stack = Stack()
    tree = BinaryTree('?') #reference to the root node 
    stack.push(tree)
    currentTree = tree #reference to a node
    for t in exp:
        # RULE 1: If token is '(' add a new node as left child
        # and descend into that node
        if t == '(':
            currentTree.insertLeft('?')
            stack.push(currentTree)
            currentTree = currentTree.getLeftTree() 
        # RULE 2: If token is operator set key of current node
        # to that operator and add a new node as right child
        # and descend into that node
        elif t in ['+', '-', '*', '/','**']:
            currentTree.setKey(t)
            currentTree.insertRight('?')
            stack.push(currentTree)
            currentTree = currentTree.getRightTree()
        # RULE 3: If token is number, set key of the current node
        # to that number and return to parent
        elif t not in ['+', '-', '*', '/', ')','**'] :
            try:
                tmp = int(t)
                currentTree.setKey(int(t))
                parent = stack.pop()
                currentTree = parent 
            except:
                tree ="Please enter a number and not any letters! Try again!"

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
        elif op =='**':
            return evaluate(leftTree) ** evaluate(rightTree)
    else:
        return tree.getKey()

def evaluate2(tree):
    leftTree = tree.getLeftTree()
    rightTree = tree.getRightTree()
    op = tree.getKey()
    if leftTree != None and rightTree != None:
        if op == '+':
            return max(evaluate2(leftTree),evaluate2(rightTree))
        elif op == '-':
            return min(evaluate2(leftTree),evaluate2(rightTree))
        elif op == '*':
            return round(evaluate2(leftTree) * evaluate2(rightTree))
        elif op == '/':
            return round(evaluate2(leftTree) / evaluate2(rightTree))
        elif op =='**':
            return evaluate2(leftTree) % evaluate2(rightTree)
    else:
        return tree.getKey()




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
            tokens = list(expression)
            tokenised = tokenising(tokens)
            print(tokenised)
            tree = buildParseTree(tokenised)
            if buildParseTree(tokenised)=="Please enter a number and not any letters! Try again!":
                print("Please enter a number and not any letters! Please try again!")
                pass
            else:
                tree.printInorder(0)
                if evaluationMode=='1':
                    print(f'The expression: {expression} evaluates to: {evaluate(tree)}')
                else:
                    print(f'The expression: {expression} evaluates to: {evaluate2(tree)}')
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