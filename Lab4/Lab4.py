"""
Course: Data Structures CS2302
Author: Laura Berrout
Assignment: Lab #2
Instructor: Dr. Olac Fuentes
T.A.:
Date of last modification: 03/15/2019
Purpose: Write functions to perform several operations with b-trees

"""
#Taken from code by Dr. Olac Fuentes
import time

class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
        
        
def height(T):
    if T.isLeaf:
        return 0
    return 1 + height(T.child[0])
        
        
def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)
                  
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
    
def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)
    
L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45, 6,300,301,7,8,9,10,11,12,13,106,107,108]
#L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80]
T = BTree()    
for i in L:
    #print('Inserting',i)
    Insert(T,i)
    #PrintD(T,'') 
    #Print(T)
    #print('\n####################################')
   


#********************************************** My code  **********************************************
# 1. Compute the height of the tree
elapsed_time = time.time()
def Heightbt(T):
    if T.isLeaf:
        return 0
    return 1 + Heightbt(T.child[0])

PrintD(T,'')
print("1) Height of b-tree: ",Heightbt(T))
print("Elapsed time: ", elapsed_time)
print()

# 2. Extract the items in the B-tree into a sorted list.
Sortedlist = []   #create list to add the elements of the b-tree
def Createlist(T,list):
	if T.isLeaf:
		for t in T.item:
			list.append(t)
	else:
		for i in range(len(T.item)):
			Createlist(T.child[i],list)
			list.append(T.item[i])
		Createlist(T.child[len(T.item)],list)
	return list
print("2) List from the B-tree:")
print(Createlist(T,Sortedlist))
print()

#3. Return the minimum element in the tree at a given depth d
#if depth is greater than height, return than depth is greater than the height of the b-tree
def MininDepth(T,depth):
	if depth==0:
		print(T.item[0])
	else:
		MininDepth(T.child[0],depth-1)
depth = 2
print("3) Minimum number in depth ", depth, ":", end=' ')
MininDepth(T,depth)
print()


# 4. Return the maximum element in the tree at a given depth d.
def MaxinDepth(T,depth):
	if depth==0:
		print(T.item[len(T.item)-1])
	else:
		MaxinDepth(T.child[len(T.child)-1],depth-1)
depth = 2
print("4) Maximum number in depth ", depth, ":",end=' ',)
MaxinDepth(T,depth)
print()

# 5. Return the number of nodes in the tree at a given depth d.
def NodesinDepth(T,depth):
	sum = 0
	if depth==0:
		return sum + len(T.item)
	else:
		for i  in range(len(T.child)):
			sum += NodesinDepth(T.child[i],depth-1)
		return sum
depth = 2
print("5) Number of nodes in depth ", depth,":",end=' ')
print(NodesinDepth(T,depth))
print()

# 6. Print all the items in the tree at a given depth d.
def PrintinDepth(T,depth):
	if depth==0:
		for i in range(len(T.item)):
			print(T.item[i],end=' ')
	else:
		for i  in range(len(T.child)):
			PrintinDepth(T.child[i],depth-1)
depth = 1
print("6) Numbers in depth ", depth,":",end=' ')
PrintinDepth(T,depth)
print()

# 7. Return the number of nodes in the tree that are full.
def Nodesfull(T):
	sum = 0
	if T.isLeaf:
		return sum
	else:
		if IsFull(T):
			sum +=1
		for i in range(len(T.child)):
			sum += Nodesfull(T.child[i])
		return sum
print()
print("7) Number of nodes full: ", end=' ')
print(Nodesfull(T))
print()

# 8. Return the number of leaves in the tree that are full.
#if the next is a leaf then check if is full
#if not, then go to the next child
def Leafsfull(T):
	sum = 0
	if T.isLeaf:
		return sum
	else:
		for i in range(len(T.child)):
			if T.child[i].isLeaf:
				if IsFull(T.child[i]):
					sum +=1
			sum +=Leafsfull(T.child[i])
		return sum

print("8) Number of leafs full: ", end=' ')
print(Leafsfull(T))
print()

# 9. Given a key k, return the depth at which it is found in the tree, of -1 if k is not in the tree
def DepthK(T,k):
	node = Search(T,k)
	depth = 0
	if node is None:
		return -1
	elif k in T.item:
		return depth
	else:
		for i in range(len(T.child)):
			depth +=1
			depth += DepthK(T.child[i],k)
		return depth
		
print("9) Key found in depth: ", end=' ')
print(DepthK(T,60))
print()
