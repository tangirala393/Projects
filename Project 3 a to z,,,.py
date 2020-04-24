



'''
print("Welcome to Pattern  Print House")

alpha = input("enter the Letter from user:")

n = int(input("enter the no of line  to Print pattern"))


### To print pattern 'A'
for row in range(5):
    for col in range(10):
        if (row==0 and (col==4  or col==5)) or (row==1  and (col==3 or col==6)) or (row==2 and (col>=2 and col<=7)) or (row==3 and (col==1 or col==8)) or (row==4 and (col==0 or col==9)):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n")

### To print pattern 'B'
for row in range(6):
    for col in range(4):
        if ((row==0 or row==4) and col<=3) or (row==2 and col<3) or ((row==1 or row==3) and (col==0 or col==3)):
            print("*",end="")
        else:
            print(end=" ")
    print()

####To print pattern 'C'
for row in range(5):
    for col in range(4):
        if (row==0 or row ==4) or col==0:
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n")


####To print pattern 'D'
for row in range(5):
    for col in range(5):
        if (col==0 or col==4) or (row==0 or row==4):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n")


####To print pattern 'E'
for row in range(5):
    for col in range(5):
        if (row==0 or row==4) or col==0 or (row==2 and col<=2):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n")
####To print pattern 'F'
for row in range(5):
    for col in range(5):
        if row==0  or col==0 or (row==2 and col<=2):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n")


####To print pattern 'H'
for row in range(5):
    for col in range(5):
        if (col==0 or col==4) or row==2:
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n")


####To print pattern 'J'
for row in range(5):
    for col in range(5):
        if (row==0 or row==4) or col==2:
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n")
'''






height = 5 
 
width = (2 * height) - 1
n=width/2
  
for i in  range(height):
        for j in range(width): 
            if (j == n or j == (width - n) or (i == height / 2 and j > n          and j < (width - n))): 
                print("*"); 
            else:
                print(" "); 
         
        print("\n"); 
        n=n-1


























