"""
Course: Data Structures CS2302
Author: Laura Berrout
Assignment: Lab #3
Instructor: Dr. Olac Fuentes
T.A.:
Date of last modification: 03/11/2019
Purpose: 
"""
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


#iterative search
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

print("Iterative Search: ")
Search(T,10,0)
print()

#Build a balanced tree
B = [10, 12, 15, 20, 30, 60, 84, 85, 90,100]
def BalanceTree(List,T):
	if len(List)==1:
		return
	else:
		num = len(List)
		middle = List[num//2-1]
		left = List[0:(num//2)]
		right = List[(num//2):len(List)]
		#print(left)
		#print(right)
		T= BST(0)
		T.item = middle
		T.left = BalanceTree(left,T.left)
		T.right = BalanceTree(right,T.right)
	return T

Tnew = BST(0)
print("Balanced BST from list: ")
InOrderD(BalanceTree(B,Tnew),' ')
print()

	
#Extracting the elements from a tree to a sorted list
Tother = BST(0)
Tother = BalanceTree(B,Tnew)
C = []
def Createlist(T,list):
	if T is not None:
		Createlist(T.left,list)
		list.append(T.item)    #insert root
		Createlist(T.right,list)
	return list
print("List from BST: ")
print(Createlist(Tother,C))
print()

#Print the elements ordered by depth
def PrintbyDepth(T,i):
	if T is not None:
		print("Keys at depth ", i, ": ",end = ' ')
		print(T.item)
		PrintbyDepth(T.left,i+1)
		PrintbyDepth(T.right,i+1)
	
PrintbyDepth(T,0)
InOrderD(T,' ')
'''
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

InOrder(T)
print()
InOrderD(T,'')
print()

print(SmallestL(T).item)
print(Smallest(T).item)

FindAndPrint(T,40)
FindAndPrint(T,110)

n=60
print('Delete',n,'Case 1, deleted node is a leaf')
T = Delete(T,n) #Case 1, deleted node is a leaf
InOrderD(T,'')
print('####################################')

n=90      
print('Delete',n,'Case 2, deleted node has one child')      
T = Delete(T,n) #Case 2, deleted node has one child
InOrderD(T,'')
print('####################################')

n=70      
print('Delete',n,'Case 3, deleted node has two children') 
T = Delete(T,n) #Case 3, deleted node has two children
InOrderD(T,'')

n=40      
print('Delete',n,'Case 3, deleted node has two children') 
T = Delete(T,n) #Case 3, deleted node has two children
InOrderD(T,'')
'''
