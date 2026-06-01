#Account=1234567890
#balance =20000
#deposite =10000
#   print("Transaction Successfull")
#else:
 #   print("Transaction Failed")
 
#Account=1234567890
#balance=20000
#deposite=int(input("Enter the amount"))
#sum=balance+deposite
#print("The sum of two number is",sum)

Aval_bal=25000
deposite=int(input("Enter deposite amount"))
Aval_bal+=deposite
withdraw=int(input("Enter withdraw amount"))
if withdraw <=Aval_bal:
    Aval_bal-=withdraw
    print("Transaction successfull")
    print("Fial_bal",Aval_bal)
else:
    print("Insufficient balance")


