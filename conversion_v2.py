
while True:
    valid=1
    print('\nSelect Option: ')
    print("Select #1 to convert to binary\nSelect #2 to convert from binary\nSelect #3 to convert from base1 to base2\n***BASES OVER 10 ARE NOT SUPPOTED***")
    option=int(input('Enter choice no.: '))
    Z=[1,2]
    S=[1,2,3]
    if option in Z:
        digit=int(input("Enter base (enter 2 for binary and 8 for octa): "))
    elif option ==3:
        base1=int(input("Enter base of input no: "))
        base2=int(input("Enter base to which the no. is to be converted: "))
    elif option not in S:
        print("Enter valid choice no.")
        
    
    if option in S:
        a=str(input('Enter input no.: '))
    
    
    
        
        M=[0,1]
        
        R=a.split(".")
        for i in range(0,len(R)):
            for q in range(0,len(R[i])):
                if option==3:
                    if int(R[i][q])<base1:
                        valid=1
                    else:
                        valid=0
                        break
                else:   
                    if int(R[i][q])<digit:
                        valid=1
                    else:
                        valid=0
                        break

        def convert(input,digit):   

            L=input.split(".")
            main=L[0]
            #print(L[0])

            #print(decimal)
            a=int(main)
            
            #CASE IF NOT ONLY DECIMAL 
            if float(input)>1:
                Q=[]
                q=a//digit
                while q != 0:
                    q=a//digit
                    rem=a%digit
                    Q.insert(0,rem)
                    a=q
                if a==1:
                    final_main=1
                else:
                    mainc=""
                    for i in Q:
                        mainc+=str(i)
                    final_main=int(mainc)
                    if float(input)%1 == 0:
                        return(final_main)
            #CASE FOR 1:
            elif float(input)==1 or float(input)==0:

                return(input)
            #Decimal Convert
            if float(input)%1 != 0:
                decimal=0
                decimal=L[1]
                d=int(decimal)*(10**(-1*(len(str(decimal)))))
                #print(d)
                l=[]
                e=d
                while e!=0:
                    b=e*digit
                    l.append(int(b//1))
                    e=b%1
                decic=""
                for i in l:
                    decic+=str(i)
                #print(decic)
                decim=int(decic)*(10**(-1*(len(str(decic)))))
                if float(input)>1:
                    return(final_main+decim)
                else:
                    return(decim)
        def invert(input,digit):
            L=input.split(".")
            main=0
            main=L[0]
            a=int(main)
            summain=0
            decimald=0     
                    
            

            #M=[0,1]
            #CASE IF NOT ONLY DECIMAL 
            
            if float(input)>1:
                length=len(main)
                for i in range(0,length):
                    summain+=(int(main[i])*(digit**(length-(i+1))))  
                if float(input)%1 == 0:
                        
                        return(summain)  
                
                
            #CASE FOR 1:
            elif float(input)==1 or float(input)==0:

                return(input)
            #Decimal Convert

            if float(input)%1 != 0:

                decimals=0
                decimals=L[1]
            
                
                        

                decimal=int(decimals)
                lengthd=len(decimals)
                for i in range(0,lengthd):
                    decimald+=int(decimals[i])*((digit)**(-1*(i+1)))

                
                if float(input)>1:
                    return(summain+decimald)
        def intercovert(base_x,base_y):
            return convert(str(invert(a,base_x)),base_y)        
            
            
        if option==1:
            if digit<=10:
                print(a, "converted to ",digit," bit is: ", convert(a,digit))
        elif option==2:
            if valid==1 and digit<=10:        
                print(a, "converted from base",digit," to decimal"," is: ", invert(a,digit))
            else:
                print("Program ended due to invalid base input")
        elif option==3:
            if valid==1 and base1<=10 and base2<=10:        

                print(a, "converted from base",base1," to base",base2," is: ", intercovert(base1,base2))
            else:
                print("Program ended due to invalid base input")


    at=str(input("Want to repeat? (yes/no): "))
    if at=="yes":
        ask=1
    else:
        ask=0
        break

if at=="no":
    print("Program ended upon user demand")
else:
    print("Program ended due to invalid input")
    
print('Thanks for using!')
    

    





















