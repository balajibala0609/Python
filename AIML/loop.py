#for loop
for i in range(0,10):
    print(i)

for i in range(0,10):
    print("hii")

#print even number from 0 to 100
for i in range(0,101):
    if i % 2 == 0:
        print(i)
        
for i in range(0,101,2):
    print(i)

#print odd number from 0 to 100
for i in range(0,101):
    if i % 2!=0:
        print(i)
        
for i in range(1,101,2):
    print(i)

#decending order
for i in range(20,0,-1):
    print(i)
    
#while loop
count=0
while count<10:
    print(count)
    count = count+1

#real time programming
stock_price = 0
while stock_price < 100:
    print(stock_price)
    stock_price = stock_price + 1

name = "india"
for i in name:
    print(i)
    
name = "india"
for i in range(0,5):
    print(name[i])

name= "india"
for i in range(0,len(name)):
   print(name[i])

    
numbers = [1, 5, 4, 8, 10, 13, 12, 15]
answer = 0

for number in range(0, len(numbers)):
    answer = numbers[number] + answer

print(answer)