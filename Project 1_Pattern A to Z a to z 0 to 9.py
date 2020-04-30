

print("***********************************************")
print("******  Welcome to Pattern  Print House *******")
print("***********************************************")


def func():
    
    print('''\nHere we have Patterns for:
                            A to Z
                            a to z
                            0 to 9

    Based on your Selection It will Print your Pattern''')


    attempts = 0
    R=0
    n1=int(input("\nEnter num of iterations To Print patterns:"))


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












        
    while attempts <n1:
       
        print("\nSelect option from  following list\n")
        print("1 for A - Z  \n2 for a - z \n3 for 0 - 9   ")
        n = int(input("\nEnter Height of character:"))

        attempts = attempts+1
        R =n1-attempts
        print("\nNo of attempts remaining:",R)
        
        l1 = int(input("\nSelect Character List from above Options  to Print:"))
        if l1==1:
            import character_A_Z as YY
            letter =input("\nselect letter in between A - Z : ")
            
            if letter == 'A':
                print(YY.pattern_A(n))
            elif letter == "B":
                print(YY.pattern_B(n))
            elif letter == "C":
                print(YY.pattern_C(n))
            elif letter == "D":
                print(YY.pattern_D(n))
            elif letter == "E":
                print(YY.pattern_E(n))
            elif letter == "F":
                print(YY.pattern_F(n))
            elif letter == "G":
                print(YY.pattern_G(n))
            elif letter == "H":
                print(YY.pattern_H(n))
            elif letter == "J":
                print(YY.pattern_J(n))
            elif letter == "L":
                print(YY.pattern_L(n))
            elif letter == "T":
                print(YY.pattern_T(n))
            else:
                print("\nSelected wrong Availability Character****Kindly select available Character:")

        elif l1 == 2:
            print("\n********Project is in progress***********")
            break
            print("\nSelect letter in between a - z ")
            attempts = attempts+1
            R =n1-attempts
            print("\nNo of attempts remaining:",R)
            
        elif l1 == 3:
            import numbers_pattern as XX
            number =input("\nSelect Number to Print Pattern 0 to 9 : ")
            if number=='0':
                print(X.pattern_0(n))
            elif number=='1':
                print(XX.pattern_1(n))
            elif number=='2':
                print(XX.pattern_2(n))
            elif number=='3':
                print(XX.pattern_3(n))
            elif number=='4':
                print(XX.pattern_4(n))
            elif number=='5':
                print(XX.pattern_5(n))
            elif number=='6':
                print(XX.pattern_6(n))
            elif number=='7':
                print(XX.pattern_7(n))
            elif number=='8':
                print(XX.pattern_8(n))
            elif number=='9':
                print(XX.pattern_9(n))
            
        else:
            print("\nSelected wrong Availability Number****Kindly select available Option:")
            

def main():
    func()
   
main()

input1=input("\nIf you want to continue  again Kindly select  YES/NO  :")
if input1== "YES":
    print(func())
else:
    print("\n**********$$$   THANK YOU VISIT AGIAN   $$$**************")







