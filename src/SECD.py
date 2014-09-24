'''
@author: Warren Koch
V00482478
October 29, 2009

SECD Machine:
Functionality is same as specified in Assignment 2.  I went with a concrete syntax parser
that takes an expression, recognizes what its top level is (i.e. ap, lambda or varref) and 
creates a node with the rest of the expression as its subtrees
(e.g. (a lambda x y) makes an "app" node with left subtree "a" and right subtree "lambda x y")

Everything else should be as specified.

Note: I didn't use a dictionary data type for Environment.  I found List easier than worrying about
learning the syntax for dictionaries.  Next time! 
'''

import re


class Node:
    def __init__(self, type, left, right=""):
        self.type = type
        self.left = left
        if type != "varref":
            self.right = right

def OneStep():
    global S,E,C,D
    
    #if C empty, restore from dump
    if C ==[]:
        if D == []:
            print("Answer: " + S[0][0]) 
            return False;
        else:
            sHead = S.pop(0)
            S,E,C,D = D[0]
            S = [sHead] + S
    else:
        expression = C.pop(0)
        
        #if ap, pop rator and rand, store to dump, create binding with rator to rand, and add the body of rator to the code
        if expression == "ap":
            rator = S.pop(0)
            rand = S.pop(0)
            #if rand is a closure
            if type(rand) != type(""):
                D = [(S,E,C,D)]
                S = []
                node = ParseConcreteSyntax(rator[0])
                if rator[1] == []:
                    E = [(node.left,rand)] 
                else:
                    E = E +[(node.left,rand)] + rator[1] 
                C = [node.right]   
            else:
                if type(rator) == type(""):
                    print("Nothing to apply. Result: (" + rator  + " " + rand + ")") 
                else:
                    print("Nothing to apply. Result: (" + rator[0]  + " " + rand + ")") 
                return     
        else:
            #the expression is a lambda term.  Determine where it is on the tree
            node = ParseConcreteSyntax(expression)
            if node.type == "varref":
                Bindings = [elem[1] for elem in E if elem[0]==node.left]
                if Bindings == []:
                    S = [node.left] + S
                else:
                    S = Bindings + S
            elif node.type == "lambda":
                S = [(expression,E)] + S
            elif node.type == "app": 
                C = [node.right] + [node.left] + ["ap"] + C
            else:
                print("ERROR!")
            
    return True
        
    
def ParseConcreteSyntax(s):
    #builds the next node in the tree based on expression s.
    #assumes correct spacing (i.e. ONLY one space between each item) and syntax

    m = re.compile("^\(((?:lambda [a-z] )*(?:(?:[a-z])|(?:\(.+ .+\)))) ((?:lambda [a-z] )*(?:(?:[a-z])|(?:\(.+ .+\))))\)$").match(s)
    if m:
        return Node("app",m.group(1),m.group(2))
    m = re.compile("^(?:lambda ([a-z]) )((?:lambda [a-z] )*(?:(?:[a-z])|(?:\(.+ .+\))))$").match(s)
    if m:
        return Node("lambda",m.group(1),m.group(2))
    m = re.compile("^([a-z])$").match(s)
    if m:
        return Node("varref",m.group(1))
            
    print("ERROR: Malformed lambda expression: " + s)
    return False

def ReadEvalPrint():
    global S,E,C,D
    PPMachine()
    while OneStep():
        PPMachine()
    print()

    
# Pretty print!
def PPMachine():
    global S,E,C,D  
      
    def printList(L):
        if L ==[]:
            return "nil"
        else:
            s = ""
            for x in L:
                if type(x)==type(""):
                    s += printExp(x.split()) + " :: "
                else:
                    s += printClosure(x) + " :: "
        return s[0:-4]
                    
    def printClosure(C):
        return "<" + printExp(C[0].split()) + "," + printBindings(C[1]) + ">"
        
    def printBindings(B): 
        if B == []:
            return "empty"
        s = ""
        for x in B:
            s += x[0] + " |-> " + printClosure(x[1]) + ", "
        return s[:-2]
    
    def printExp(E):
        if E == []:
            return ""
        x = E.pop(0)
        if x.find("lambda") >= 0:
            return x.replace("lambda","%",1) + E.pop(0) + "." + printExp(E)
        else:
            return x + " " + printExp(E)
        
    def printDump(D):
        if D==[]:
            return "empty"
        return "(" + printList(D[0][0]) + ", " + printBindings(D[0][1]) + ", " + printList(D[0][2]) + ", " + printDump(D[0][3]) + ")"
    
    print("S =", printList(S))
    print("E =", printBindings(E))
    print("C =", printList(C))
    print("D =", printDump(D))
    print()
 
 
    
#This is just a spare function to check that a lambda expression is being parsed properly. 
#Feel free to use it to test my parser
def PrintWholeLambda(s, d=0):
    n =ParseConcreteSyntax(s)
    print("  "*d + n.type + ": " + s)
    if (n.type !="varref"):
        PrintWholeLambda(n.left,d+1)
        PrintWholeLambda(n.right,d+1)
        
        
        



#MAIN 

S = []
E = []
C = ["(lambda a a lambda b b)"]
D = []
ReadEvalPrint()

S = []
E = []
C = ["((lambda a a lambda b b) lambda c c)"]
D = []
ReadEvalPrint()


S = []
E = []
C = ["(lambda a a (lambda b b lambda c c))"]
D = []
ReadEvalPrint()


S = []
E = []
C = ["((lambda a lambda b (b a) lambda d d) lambda c c)"]
D = []
ReadEvalPrint()



