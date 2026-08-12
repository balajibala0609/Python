#voting age
age=25
if age>=18:
    print("he can vote")
else:
    print("he can't vote")
    
#write a python program to check if a number is even or odd,get input from user
number = int(input("enter the number"))
if number % 2 == 0:
    print("number is even")
else:
    print("number is odd" )
    
#your an instagram analyser, find the password is right or wrong from the input which user can give
original_password="balaji2005"
password_checking=input("enter the password:")
if password_checking == original_password:
    print("password correct")
else:
    print("incorrect password")

marks=int(input("enter mark"))
if marks >= 0 and marks< 40:
    print("fail")
elif marks>=40 and marks <80:
    print("distinction")
elif marks >=80 and marks <=100:
    print("first class")
else:
    print("invalid marks")


number = 80
if number > 50:
    print("1")
elif number > 60:
    print("2")
else:
    print("3")

x= 15
if x>10:
    print("A")
    
if x>12:
    print("B")
else:
    print("C")

age=80
if age >60:
    print("senior citizen")
    if age > 90:
       print("super senior citizen")
    else:
       print("normal")
else:
    print("number less then 60")
 
price = float(input("Enter the price of the item: "))
total = price * quantity
print("Your total cost is:", total)

marks=int(input("enter the marks"))
if marks <0 or marks >100:
    print("invalid marks")
elif marks >=80:
    print("distinction")
elif marks >=40:
    print("first class")
else:
    print("fail")    
 
x= 10

if x > 5:
    if x > 15:
        print("A")
else:
    print("B") 
    
age = 20
is_eligible = False

if age >= 18 and is_eligible:
   print("A") 
elif age >= 18 or is_eligible:
    print("B")
else:
    print("C")   

#write a python program to determine whether a personis rligible for a driving license conditions;
#if the person is below 18, print"not eligible"
#if the person is 18 or above and has a valid id proof, print"eligible"
#if the person is 18 or above but does not have a valid id proof, print"bring valid id proof"
#othervise, print"invalid"
age= int(input("enter the age"))
has_id= input("enter True or False")
if age  < 18:
    print("not eligible")

elif age >=18 and has_id:
    print("eligible")

elif age >= 18 and not has_id:
    print("bring valid id")
    
else:
    print("invalid input")     