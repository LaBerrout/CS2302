"""
Course: Data Structures CS2302
Author: Laura Berrout
Assignment: Lab #3
Instructor: Dr. Olac Fuentes
T.A.:
Date of last modification: 03/11/2019
Purpose: Binary Search Tree 
"""
import time

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left    
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    return T
         
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')
  
def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T   
 
def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)

def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)   

def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item == k:
        return T
    if T.item<k:
        return Find(T.right,k)
    return Find(T.left,k)
    
def FindAndPrint(T,k):
    f = Find(T,k)
    if f is not None:
        print(f.item,'found')
    else:
        print(k,'not found')
    
# Code to test the functions above
T = None
A = [70, 50, 90, 130, 150, 40, 10, 30, 100, 180, 45, 60, 140, 42]
for a in A:
    T = Insert(T,a)

#InOrderD(T,'')

#****************************************** My Code ******************************************
#1) Display the bst as the figure


#2) iterative search
def Search(T,k,level):
	if T is None:
		print("Item not found")
		return -1
	if T.item==k:
		print("Item", T.item,"found in level:" ,level)
		return level
	if T.item<k:
		print("Item ", T.item,"level:" ,level)
		return Search(T.right,k,level+1)
	else:
		print("Item ", T.item,"level:" ,level)
		return Search(T.left,k,level+1)

print("2) Iterative Search: ")
Search(T,10,0)
print()
Search(T,11,0)
print()
Search(T,70,0)
print()
start = time.time()
Search(T,150,0)

print()

#3) Build a balanced tree
B = [10, 12, 15, 20, 30, 60, 84, 85, 90,100]
B2 = [10, 12, 15, 20, 30]
B3 = [10, 12, 15, 20, 30, 60, 84, 85, 90,100, 120, 150, 154, 156, 160, 184, 200, 201, 215, 230]

def BalanceTree(List,T):
	if len(List)==1:
		return
	else:
		num = len(List)
		middle = List[num//2-1]
		left = List[0:(num//2)]
		right = List[(num//2):len(List)]
		T= BST(0)
		T.item = middle
		T.left = BalanceTree(left,T.left)
		T.right = BalanceTree(right,T.right)
	return T

Tnew = BST(0)
print("3) Balanced BST from list: ")
InOrderD(BalanceTree(B,Tnew),' ')
print()
InOrderD(BalanceTree(B2,Tnew),' ')
print()

InOrderD(BalanceTree(B3,Tnew),' ')

print()
	
#4) Extracting the elements from a tree to a sorted list

Tother = BST(0)
Tother = BalanceTree(B,Tnew)
C = []
def Createlist(T,list):
	if T is not None:
		Createlist(T.left,list)
		list.append(T.item)    #insert root
		Createlist(T.right,list)
	return list
print("4) List from BST: ")

print(Createlist(Tother,C))

print()

#5) Print the elements ordered by depth
def PrintinDepth(T,depth):
	if T is None:
		return
	else:
		if depth==0:
			print(T.item,end=' ')
		else: 
			PrintinDepth(T.left,depth-1)
			PrintinDepth(T.right,depth-1)

def PrintbyDepth(T,i):
	lent = LenTree(T)
	if i>lent:
		return
	else:
		print("Keys at depth ", i,": ",end=' ')
		PrintinDepth(T,i)
		print()
		PrintbyDepth(T,i+1)


def LenTree(T):
	lent = 0
	if T is None:
		return lent
	else:
		lent+=1
		lent +=LenTree(T.left)
		#LenTree(T.right)
	return lent


print("5) Print by Depth: ")
#PrintinDepth(T,3)
PrintbyDepth(Tother,0)
print()
start = time.time()

PrintbyDepth(T,0)

end = time.time()
print("Time: ",end-start)
print()
#print("Length: ",LenTree(T))
#InOrderD(T,' ')
