"""
Course: Data Structures CS2302
Author: Laura Berrout
Assignment: Lab #1
Instructor: Dr. Olac Fuentes
T.A.:
Date of last modification: 02/08/2019
Purpose: Use recursion to draw interesting figures
"""

import numpy as np
import matplotlib.pyplot as plt
import math

#Recursion method to draw squares
def draw_squares(ax,n,p,w):
    """
    Where:
    - ax is the axis
    - n is the number of figures
    - p array of coordinates
    - w relation of the distance between points
    """
    if n>0:
        i1 = [1,2,3,0,1]
        q = p*w + p[i1]*(1-w)
        ax.plot(p[:,0],p[:,1],color='k',linewidth=0.5)
        draw_squares(ax,n-1,q,w)

#Figure Square a
plt.close("all") 
orig_size = 800
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,10,p,.2)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Fig_Square_A.png')

#Figure Square b
plt.close("all") 
orig_size = 800
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,10,p,.1)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Fig_Square_B.png')

#Figure Square c
plt.close("all") 
orig_size = 800
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,100,p,.05)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Fig_Square_C.png')

#Recursion method to draw circles
def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_circles(ax,n,center,radius,w):
    """
    Where:
    - ax is the axis
    - n is the number of figures
    - center 
    - radius
    - w is relation of the distance between points
    """
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k',linewidth=0.5)
        draw_circles(ax,n-1,center,radius*w,w)

#Figure Circle A
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 3, [100,0], 100,.5)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Fig_Circle_A.png')

#Figure Circle B
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 50, [100,0], 100,.9)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Fig_Circle_B.png')

#Figure Circle B
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 100, [100,0], 100,.95)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Fig_Circle_C.png')

#Recursion method to draw squares with more squares at the corners
# calls the method and then calls but taking the coordinates of the new square
def draw_corners(ax,n,p,w,o): #for re-call of each square -> n
    if n>0:
        draw_squaresur(ax,1,p,w,o)
        
        n = n-1
        o1 = o*0.25
        o2 = o*0.75
        
        q = p*w + [-o1,o2] #upper left corner
        draw_corners(ax,n,q,w,o)
        
        q = p*w + (o2) #upper right corner
        draw_corners(ax,n,q,w,o)
        
        q = p*w - (o1) #lower left corner
        draw_corners(ax,n,q,w,o)
        
        q = p*w + [o2,-o1] #lower right corner
        draw_corners(ax,n,q,w,o)
        
    
def draw_squaresur(ax,n,p,w,o):
    if n>0:
        ax.plot(p[:,0],p[:,1],color='k',linewidth=0.5)
        draw_squaresur(ax,n-1,p,w,o)
        
def draw_squaresll(ax,n,p,w,o):
    if n>0:
        ax.plot(p[:,0],p[:,1],color='k',linewidth=0.5)
        draw_squaresll(ax,n-1,p,w,o)
        
def draw_squaresul(ax,n,p,w,o):
    if n>0:
        ax.plot(p[:,0],p[:,1],color='k',linewidth=0.5)
        draw_squaresul(ax,n-1,p,w,o)

def draw_squareslr(ax,n,p,w,o):
    if n>0:
        ax.plot(p[:,0],p[:,1],color='k',linewidth=0.5)
        draw_squareslr(ax,n-1,p,w,o)



#Figure Square_Corner a
plt.close("all") 
orig_size = 800
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_corners(ax,2,p,0.5,orig_size) 
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Fig_CornerSquares_A.png')


#Figure Square_Corner a
plt.close("all") 
orig_size = 800
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_corners(ax,3,p,0.5,orig_size) 
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Fig_CornerSquares_B.png')


#Figure Square_Corner a
plt.close("all") 
orig_size = 800
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_corners(ax,4,p,0.5,orig_size) #does not need to modify w
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Fig_CornerSquares_C.png')


#Method to draw circle
def circle2(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = (center[0]+rad)+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

#Recursion method to draw tangent circles
def draw_circles2(ax,n,center,radius,w):
    """
    Where:
    - ax is the axis
    - n is the number of figures
    - center 
    - radius
    - w is relation of the distance between points
    """
    if n>0:
        x,y = circle2(center,radius)
        ax.plot(x,y,color='k',linewidth=0.5)
        draw_circles2(ax,n-1,center,radius*w,w)

#Figure Circle A
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles2(ax, 10, [100,0], 100,.60)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Fig_TangentCircle_A.png')

#Figure Circle B
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles2(ax, 50, [100,0], 100,.90)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Fig_TangentCircle_B.png')

#Figure Circle C
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles2(ax, 100, [100,0], 100,.95)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Fig_TangentCircle_C.png')

#Recursive method to draw a tree, n is the number of levels
def draw_invtree(ax,p,n,size):    
    if n>0:
        size1 = [size[0]/n,size[1]/n]

        p = np.array([[size[0]/4,(n-1)*(size[1]/n)],[size[0]/2,size[1]],[(3*size[0])/4,(n-1)*(size[1]/n)]])
        print("new size: ", size1)
        draw_lines(ax,p,size1)
        n=n-1
        draw_invtree(ax,p,n,size1) #draws the left side
        
'''
        p = np.array([[size[0]/4,(n-1)*(size[1]/n)],[size[0]/2,size[1]],[(3*size[0])/4,(n-1)*(size[1]/n)]])
        draw_lines(ax,p,size)
'''        


def draw_lines(ax,p,size): #left side
        print("points coordindates: ")
        print(p)
        ax.plot(p[:,0],p[:,1],color='k',linewidth=0.5)



#Figure Square a
plt.close("all") 
orig_size = 800
size = [orig_size,orig_size]
print("size:",size)
n = 2  #number of levels
#p = np.array([[orig_size//(2**(n+1)),(orig_size//n) - (orig_size//n)], [2*orig_size//2**(n+1),orig_size//n],[3*orig_size//2**(n+1),(orig_size//n) - (orig_size//n)]])
p = np.array([[size[0]/4,size[1]-(size[1]/n)],[size[0]/2,size[1]],[(3*size[0])/4,size[1]-(size[1]/n)]])
fig, ax = plt.subplots()
draw_invtree(ax,p,n,size)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('Fig_Invtree_A.png')




#Recursion method to draw circles
def draw_circles(ax,n,center,radius,w):
    if n>0:
        circle3(center,radius)
       
        n=n-1
        w = radius/3
        radius = radius/3
        center1 = [center[0]+(2*radius),center[1]]
        center2 = [center[0]-(2*radius),center[1]]
        center3 = [center[0],center[1]+(2*radius)]
        center4 = [center[0],center[1]-(2*radius)]
        
        draw_circles(ax,n,center,radius,w) #draws circle at the center
        draw_circles(ax,n,center1,radius,w) #draws right circle   
        draw_circles(ax,n,center2,radius,w) #drawa left circle
        draw_circles(ax,n,center3,radius,w) #drawa upper circle
        draw_circles(ax,n,center4,radius,w) #drawa down circle

       

def circle3(center,rad):
        n = int(4*rad*math.pi)
        t = np.linspace(0,6.3,n)
        x1 = (center[0])+rad*np.sin(t)
        y1 = center[1]+rad*np.cos(t)
        ax.plot(x1,y1,color='k',linewidth=0.5)
        return x1,y1


#Figure Circle A
plt.close("all") 
fig, ax = plt.subplots() 
radius = 100
n = 3
w = radius/3
draw_circles(ax, n, [100,0], radius, w)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Fig_InsideCircle_A.png')

plt.close("all") 
fig, ax = plt.subplots() 
radius = 100
n = 4
w = radius/3
draw_circles(ax, n, [100,0], radius, w)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Fig_InsideCircle_B.png')

plt.close("all") 
fig, ax = plt.subplots() 
radius = 100
n = 5
w = radius/3
draw_circles(ax, n, [100,0], radius, w)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Fig_InsideCircle_C.png')



