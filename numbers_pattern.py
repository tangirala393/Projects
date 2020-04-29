

    
def pattern_0(n):
    for i in range(n):
        for j in range(n):
            if  (((j==0 or j==n-1) and (i!=0 and i!=n-1)) or
                ((i==0 or  i==n-1) and (j>0 and j<n-1))): 
                print("*",end="")

            else:
                print(" ",end="")
        print()

        
def pattern_1(n):
   for i in range(n):
        for j in range(n):
            if (i>=0 and j==n//2) : 
                print("*",end="")
            else:
                print(" ",end="")
        print()


    
def pattern_2(n):
    for i in range(n):
        for j in range(n):
            if  ((i==0 or i==n-1 or  i==n//2) or
                 ((i>0 and i<n//2) and j==n-1) or
                 ((i>n//2 or i==n-1) and j==0)):
                print("*",end="")

            else:
                print(" ",end="")
        print()


    
def pattern_3(n):
    for i in range(n):
        for j in range(n):
        
            if i==0 or i==n-1 or i==n//2 or j==n-1:
                print("*",end="")

            else:
                print(" ",end="")
        print()


def pattern_4(n):
    for i in range(n):
        for j in range(n):
            if ((i==n//2 or j==n-1)or
                (j==0 and (i>=0 and i<n//2))):
                print("*",end="")

            else:
                print(" ",end="")
        print()

        
def pattern_5(n):
   for i in range(n):
        for j in range(n):
            if  ((i==0 or i==n-1 or  i==n//2) or
                 ((i>0 and i<n//2) and j==0) or
                 ((i>n//2 or i==n-1) and j==n-1)):
                print("*",end="")

            else:
                print(" ",end="")
        print()

   
def pattern_6(n):
    for i in range(n):
        for j in range(n):
            if  ((i==0 or i==n-1 or  i==n//2) or
                 (j==n-1 and (i>n//2 or i==n-1)) or
                 (j==0 and (i>0 and i<n-1))):
                print("*",end="")

            else:
                print(" ",end="")
        print()


def pattern_7(n):
    for i in range(n):
        for j in range(n):
            if  i==0 or j==n-1:
                
                print("*",end="")

            else:          
                print(" ",end="")
        print()

   
def pattern_8(n):
    for i in range(n):
        for j in range(n):
            if (i>0 and j==0) or(i==0 and j<n) or(i==n//2 and j<n) or(i==n-1 and j<n) or j==n-1: 
                print("*",end="")
            else:
                print(" ",end="")
        print()

  
def pattern_9(n):
    for i in range(n):
        for j in range(n):
            if  ((i==0 or i==n-1 or  i==n//2) or
                 ((i>0 or i<n//2) and j==n-1 ) or
                 (j==0 and (i>0 and i<n//2))):
                print("*",end="")

            else:
                print(" ",end="")
        print()






