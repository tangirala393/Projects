# Python3 program to print alphabet A pattern
# Function to display alphabet pattern 
def pattern_A(n): 
  
    # Outer for loop for number of lines 
    for i in range(n): 
  
        # Inner for loop for logic execution 
        for j in range((n // 2) + 1): 
  
            # prints two column lines 
            if ((j == 0 or j == n // 2) and i != 0 or
                
                  
                # print first line of alphabet 
                i == 0 and j != 0 and j != n // 2 or
  
                # prints middle line 
                i == n // 2): 
                print("*", end = "") 
            else: 
                print(" ", end = "") 
          
        print()    
######## End-of-A ########

# Python3 program to print alphabet B pattern
# Function to display alphabet pattern 
def pattern_B(n):
    for i in range(n):
        for j in range(n):
            if ((j==0 or i>=n) or
                (i==n//2 and  j<n//2) or
                 ((i==0 or i==n-1) and j< n//2) or
                 ((i>0 and i<n//2) or (i>=n//2 and  i<=n-2)) and
                  (j<=0 or  j==(n//2))):
                print("*",end="")

            else:
                print(" ",end="")
        print()
######## End-of-B ########

# Python3 program to print alphabet C pattern
# Function to display alphabet pattern 
def pattern_C(n):
    for i in range(n):
        for j in range(n):
            if ((i>0 and i<n-1 and j==0) or
                ((i==0 or i==n-1) and ((j>0) and (j<=n//2)))):
                
                print("*",end="")

            else:
                print(" ",end="")
        print()
######## End-of-C ########


# Python3 program to print alphabet D pattern
# Function to display alphabet pattern 
def pattern_D(n):
    for i in range(n):
        for j in range(n):
            if ((j==0 ) or 
                (j==n//2 and i!=0 and i!=n-1) or
                (i==0 or i==n-1) and (j>0 and j<=n//2-1)) :
                    
                print("*",end="")

            else:
                print(" ",end="")
        print()
######## End-of-D ########

        

# Python program to print pattern G 
def pattern_G(n): 
    for i in range(0,n):     
        for j in range(0,n):      
            if ((j == 1 and i != 0 and i != n-1) or ((i == 0 or
                i == n-1) and j > 1 and j < n-2) or (i == ((n-1)/2) 
                and j > n-5 and j < n-1) or (j == n-2 and
                i != 0 and i != n-1 and i >=((n-1)/2))):   
                print("*", end = "") 
            else: 
                print(" ", end = "") 
          
        print()
    
######## End-of-G ########

# Python3 program to print alphabet E pattern 
# Function to display alphabet pattern 
def pattern_E(n):
    #n=int(input("enter the row and col size:"))
    for row in range(0,n):
        for col in range(0,n):
            if(col==1 or((row==0 or row==n-1)and(col>1 and col<n-1))or(row==n//2 and col>1 and col<n-2)):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            
        print()
######## End-of-E ########


# Python3 program to print alphabet F pattern 
# Function to display alphabet pattern 
def pattern_F(n):
    for row in range(0,n):
        for col in range(0,n):
            if(col==1 or((row==0)and(col>1 and col<n-1))or(row==n//2 and col>1 and col<n-2)):
                print("*",end=" ")
            else:
                print(" ",end=" ")
                
        print()
######## End-of-F ########


# Python3 program to print alphabet H pattern 
# Function to display alphabet pattern
def pattern_H(n):

    for i in range(n):
        for j in range(n):
            if j==0 or j==n//2+1 or (i==n//2 and j<=n//2):
                    
                print("*",end="")

            else:
                    print(" ",end="")
        print()
######## End-of-H ########

# Python3 program to print alphabet I pattern 
# Function to display alphabet pattern

def pattern_I(n):
    
    for i in range(n):
        for j in range(n):
            if (i==0 or i==n-1) or j==n//2: 
                print("*",end="")

            else:
                print(" ",end="")
        print()
######## End-of-I ########


# Python3 program to print alphabet J pattern
def pattern_J(n):
    for i in range(n):
        for j in range(n):
            if ((i==0  or j==n//2) or
                (i==n-1 and j<=n//2)): 
                print("*",end="")

            else:
                print(" ",end="")
        print()
######## End-of-J ######
        
  
# Python3 program to print alphabet L pattern 
# Function to display alphabet pattern
def pattern_L(n):
    for i in range(n):
        for j in range ((n//2)+1):
            if (i<=n and j==0) or (i==(n-1) and j<=n):
            #if (j==0 and  i<n) or (i==n and j<n//2):
                print("*", end = "") 
            else: 
                print(" ", end = "") 
          
        print()
    return
    
######## End-of-L ########


    

# Python3 program to print alphabet T pattern 
# Function to display alphabet pattern 
def pattern_T(n):
    #n=int(input("enter the row and col size:"))
    for row in range(0,n):
        for col in range(0,n):
            if(row==0 or col>n)or col==n//2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
                
        print()
######## End-of-T ########
