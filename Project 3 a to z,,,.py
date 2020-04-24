



'''
print("Welcome to Pattern  Print House")

alpha = input("enter the Letter from user:")

n = int(input("enter the no of line  to Print pattern"))
'''

### To print pattern 'A'
print("Pattern for A")
for row in range(5):
    for col in range(10):
        
        if (row==0 and (col==4  or col==5)) or (row==1  and (col==3 or col==6)) or (row==2 and (col>=2 and col<=7)) or (row==3 and (col==1 or col==8)) or (row==4 and (col==0 or col==9)):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n")

### To print pattern 'B'
print("Pattern for B")
for row in range(6):
    for col in range(4):
        if ((row==0 or row==4) and col<=3) or (row==2 and col<3) or ((row==1 or row==3) and (col==0 or col==3)):
            print("*",end="")
        else:
            print(end=" ")
    print()

####To print pattern 'C'

print("Pattern for C")
for row in range(5):
    for col in range(4):
        if (row==0 or row ==4) or col==0:
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n")


####To print pattern 'D'
print("Pattern for D")
for row in range(5):
    for col in range(5):
        if (col==0 or col==4) or (row==0 or row==4):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n")


####To print pattern 'E'
print("Pattern for E")
for row in range(5):
    for col in range(5):
        if (row==0 or row==4) or col==0 or (row==2 and col<=2):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n")
####To print pattern 'F'
print("Pattern for F")
for row in range(5):
    for col in range(5):
        if row==0  or col==0 or (row==2 and col<=2):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n")


####To print pattern 'H'
print("Pattern for H")
for row in range(5):
    for col in range(5):
        if (col==0 or col==4) or row==2:
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n")


####To print pattern 'J'
print("Pattern for J")
for row in range(5):
    for col in range(5):
        if (row==0 or row==4) or col==2:
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n")


####To print pattern 'K'
print("Pattern for K\n")

for row in range(5):
    for col in range(4):
        if (row<5 and col==0) or (row==2 and col==1) or ((row==0 or row==4) and col==3) or ((row==1  or row==3) and col==2):
        
                print("*",end="")
        else:
            print(end=" ")
    print()
print("\n")



####To print pattern 'L'
print("Pattern for L\n")

for row in range(5):
    for col in range(4):
        if (row<5 and col==0) or (row==4 and col<5):
        
                print("*",end="")
        else:
            print(end=" ")
    print()
print("\n" ) 


####To print pattern 'M'
print("Pattern for M\n")

for row in range(5):
    for col in range(5):
        if (row<5 and (col==0 or col==4)) or (row==col!=3) or  (row==1 and col==3):
        
                print("*",end="")
        else:
            print(end=" ")
    print()
print("\n" )


####To print pattern 'N'
print("Pattern for N\n")

for row in range(5):
    for col in range(5):
        if (row<5 and (col==0 or col==4)) or (row==col):
        
                print("*",end="")
        else:
            print(end=" ")
    print()
print("\n" )



####To print pattern 'o'
print("Pattern for o\n")

for row in range(5):
    for col in range(5):
        if (( row>0 and row<5) and (col==0  or col==4)) or ((row==0 and  row==4) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n" )


####To print pattern 'P'
print("Pattern for P\n")
for row in range(5):
    for col in range(5):
        if (row>=0 and col==0) or ((row==0 or row==2) and col<3) or (row==1 and col==3):
        
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n" )

####To print pattern 'S'
print("Pattern for S\n")
for row in range(7):
    for col in range(6):
        if ((row==0 or row==3 or row==6) and (col>0 and col<5)) or (col==0 and (row==1 or row==2 or row==5)) or (col==5 and (row==1 or row==4 or row==5)):
        
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n" )


####To print pattern 'T'
print("Pattern for T\n")
for row in range(5):
    for col in range(5):
        if (row==0 or col>5) or (col==2 or row>5):
        
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n" )


####To print pattern 'U'
print("Pattern for U\n")
for row in range(5):
    for col in range(5):
        if (row<4 and (col==0 or col==4)) or (row==4 and (col>0 and col<4)):
        
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n" )


####To print pattern 'V'
print("Pattern for V\n")
for row in range(5):
    for col in range(9):
        if (row==col) or (row<4 and (col>4 and col<9)):
        
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n" )































