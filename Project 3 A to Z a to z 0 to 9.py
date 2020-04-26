
print("***********************************************")
print("******  Welcome to Pattern  Print House *******")
print("***********************************************")

attempts = 0
R=0

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
    
######## End-of-L ########

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
# Python3 program to print alphabet F pattern 
# Function to display alphabet pattern 
def pattern_F(n):
    #n=int(input("enter the row and col size:"))
    for row in range(0,n):
        for col in range(0,n):
            if(col==1 or((row==0)and(col>1 and col<n-1))or(row==n//2 and col>1 and col<n-2)):
                print("*",end=" ")
            else:
                print(" ",end=" ")
                
        print()
    

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


  
   
while attempts <3:
    print("\nSelect option from  following list\n")
    print("1 for A - Z   (A,G,L,E,F,T)\n2 for a - z   (in progress)\n3 for 0 - 9   (in progress)")
    n = int(input("\nEnter Height of character:"))

    attempts = attempts+1
    R =3-attempts
    print("\nNo of attempts remaining:",R)
    
    l1 = int(input("\nSelect Character List from above Options  to Print:"))
    if l1==1:
        letter =input("\nselect letter in between A - Z : ")
        #attempts = attempts+1
        #R =3-attempts
        #print("\nNo of attempts remaining:",R)

        if letter == 'A':
            pattern_A(n)

        elif letter == "G":
            pattern_G(n)
            
        elif letter == "L":
            pattern_L(n)
        elif letter == "E":
            pattern_E(n)
        elif letter == "F":
            pattern_F(n)
        elif letter == "T":
            pattern_T(n)
            

       # elif letter != 'A' !='G' !='L':
        else:
            print("\nSelected wrong Availability Character****Kindly select available Character:")
        
    elif l1 == 2:
        print("\n********Project is in progress*********")
        break
        print("\nSelect letter in between a - z ")
        attempts = attempts+1
        R =3-attempts
        print("\nNo of attempts remaining:",R)

    elif l1 == 3:
        print("\n********Project is in progress***********")
        break
        print("\nselect letter in between 0 - 9 ")
        R =3-attempts
        print("\nNo of attempts remaining:",R)

    else:
        print("\nSelected option is not available Kindly select Proper Option")
        attempts = attempts+1
        R =3-attempts

        print("\nNo of attempts remaining:",R)
input1=input("\n If you want to continues the loop again give YES/NO  :")


if input1== "YES":
    print()
else:
    print("\n**********$$$   THANK YOU VISIT AGIAN   $$$**************")










