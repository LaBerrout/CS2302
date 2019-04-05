"""
Course: Data Structures CS2302
Author: Laura Berrout
Assignment: Lab #2
Instructor: Dr. Olac Fuentes
T.A.: Anindita Nath
Date of last modification: 02/22/2019

Purpose: implement several algorithms for 
nding the median of a list of 
integers, using objects of the List class described in class, and compare 
their running times (measured as the number of comparisons each algorithm 
makes) for various list lengths. To generate data to test your methods, 
write a method that receives an integer n and builds and returns a list of 
random integers of length n.

"""
import random
import time

#List of class objects 
class Node(object):
    def __init__(self,item,next=None):
        self.item = item
        self.next = next

class List(object):
    def __init__(self):
        self.head = None
        self.tail = None

def IsEmpty(L):
    return L.head == None

def Append(L,x):
    #Inserts at the end
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next

def Remove(L,x):
    # Removes x from list L
    # It does nothing if x is not in L
    if L.head==None:
        return
    if L.head.item == x:
        if L.head == L.tail: # x is the only element in list
            L.head = None
            L.tail = None
        else:
            L.head = L.head.next
    else:
         # Find x
         temp = L.head
         while temp.next != None and temp.next.item !=x:
             temp = temp.next
         if temp.next != None: # x was found
             if temp.next == L.tail: # x is the last node
                 L.tail = temp
                 L.tail.next = None
             else:
                 temp.next = temp.next.next

def Push(self,new_data):
    #Inserts at the beginning
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node
    
def Insert(self,new_data,location):  #inserts an element in a specific location
    position = 2
    tmp = self.head
    new_node = Node(new_data)
    while position < location:
        position +=1
        tmp = tmp.next
    tmp2 = tmp.next
    tmp.next = new_node
    new_node.next = tmp2
    

def Print(L):
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()
    
def Copy(L):
    temp = L.head
    new_list = List()
    while temp.next is not None:
        Append(new_list,temp.item)
        temp = temp.next
    Append(new_list,temp.item)
    return new_list
        


    
# ********************************************** Sort Algorithms  **********************************************
#Create a list of size n with random numbers
A = List()
n = 9
for i in range(n):
    rand = random.randrange(101)
    Append(A,rand)

print("Random List:")
Print(A)
print()

AL = []
def ListArray(AL,L):
	tmp = L.head
	i=0
	while tmp is not None:
		AL.append(tmp.item)
		tmp = tmp.next

def Getmiddle(L,n):
	tmp = L.head
	mid = n//2
	i=0
	while tmp.next is not None:
		if i==mid:
			print(tmp.item)
			return
		else:
			i+=1
			tmp = tmp.next
#Getmiddle(A,n)

		
#1) Bubble Sort    
         
def BubbleSort(self):
    sorted = False
    while sorted != True:
        count = 0
        tmp = self.head
        while tmp.next is not None:
            if (tmp.item > tmp.next.item):
                save = tmp.item
                tmp.item = tmp.next.item
                tmp.next.item = save
                count +=1
            tmp = tmp.next
        if count == 0:
            sorted = True
			

B = Copy(A)
print("1) By Bubble Sort:")
BubbleSort(B)
Print(B)
print("Element in the middle: ", end=' ')
Getmiddle(B,n)

print()


#2) Merge Sort
def Length(L):
    tmp = L.head
    count = 0
    while tmp.next is not None:
        count +=1
        tmp = tmp.next
    return count

def Split(self):              #divides a list by half and returns two lists
	tmp = self.head
	n = Length(self)        #n is the number of elements in the list
	if n==1:
		return self
	else:
		mid = n//2  +1             #midpoint of the list
		L1 = List()
		L2 = List()
		count = 0
		while count < mid:
			Append(L1,tmp.item)
			tmp = tmp.next
			count +=1
		tmp = self.head
		for i in range(mid+1):
			L2.head = tmp
			tmp = tmp.next
		return L1,L2

def MergeSort(self):
	n = Length(self)
	left=List()
	right=List()
	Sorted = List()
	tmp = self.head
	if n<1:
		return self
	elif n==1:
		Append(left,tmp.item)
		tmp = tmp.next
		Append(right,tmp.item)
	else:
		left, right = Split(self)
		MergeSort(left)
		MergeSort(right)
		Sorted = Sort(left,right)
		return Sorted

def Sort(L1,L2):  #sorted the two lists and returns one list
	tmp1 = L1.head
	tmp2 = L2.head
	Sorted = List()
	while tmp1 is not None and tmp2 is not None:
		if tmp1.item <= tmp2.item:
			Append(Sorted,tmp1.item)
			tmp1 = tmp1.next
		else:
			Append(Sorted,tmp2.item)
			tmp2 = tmp2.next
	while tmp1 is not None:
		if tmp1 is not None:
			Append(Sorted,tmp1.item)
		tmp1 = tmp1.next
	while tmp2 is not None:
		if tmp2 is not None:
			Append(Sorted,tmp2.item)
		tmp2 = tmp2.next
	return Sorted
	
def Sorttt(L):
	tmp = L.head
	while tmp.next is not None:
		if tmp.item>tmp.next.item:
			MergeSort(L)
		tmp = tmp.next
	return L
		
B = Copy(A)
Sorted = List()
start = time.time()
Sorted = MergeSort(B)
Sorted = MergeSort(Sorted)
Sorted = MergeSort(Sorted)
Sorted = MergeSort(Sorted)
#Sorted = Sorttt(Sorted)
Sorted = MergeSort(Sorted)

print("2) By Merge Sort:")
Print(Sorted)
print("Element in the middle: ", end=' ')
Getmiddle(Sorted,n)
end = time.time()
print("Time: ", end=' ')
print(end)
print()  


#3) QuickSort
def QuickSort(L,n):
    if L.head is None or L.head.next is None:
        return L
    tmp = L
    pivot = L.head.item
    left = 0                              #left pointer
    right = n                             #right pointer
    lelement = tmp.head.item                 #first element
    relement = tmp.tail.item                 #last element
    if (lelement > pivot):
        swapping =  lelement
        lelement = relement
        relement = swapping
    if (relement < pivot):
        swapping = relement
        relement = lelement
        lelement = swapping
    return tmp

def partition(L,low,high): 
	i = ( low-1)		 # index of smaller element 
	pivot = L[high]	 # pivot 
	for j in range(low , high): 
		if L[j] <= pivot: 
			i = i+1
			L[i],L[j] = L[j],L[i] 

	L[i+1],L[high] = L[high],L[i+1] 
	return ( i+1 ) 

def Sort(L,low,high): 
	if low < high: 
		mid = partition(L,low,high) 
		Sort(L, low, mid-1) 
		Sort(L, mid+1, high) 
	
	
D = Copy(A)
print("3) By QuickSort:")
#QuickSort(D,n)
#Print(D)

DL =[]
ListArray(DL,D)
Sort(DL,0,len(DL)-1)
Dsort = List()
for i in range(n):
    Append(Dsort,DL[i])
Print(Dsort)

print("Element in the middle: ", end=' ')
Getmiddle(Dsort,n)
