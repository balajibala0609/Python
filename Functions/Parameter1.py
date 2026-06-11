#function with default parameter
#def register(name,location,prefix="mr/mrs/miss"):
 #   if location == 'bangalore':
  #      print(prefix,name,"Has approved in",location)
   # elif location == 'hydrabad':
    #    print(prefix,name,'Relocation the hydrabad',location)
    #else:
     #   print("Business not approved")
#register('cts','bangalore')
#register('tcs','hydrabad','mr')
#register("finish",'balaji')

#banking
amount=[15000,25000,45000,3000]
def debit(money=0,pos=0):
    if money <= amount[pos]:
        amount[pos]-=money
        print(money,'amount')
        return amount[pos]
    else:
        print("cannot debit")
bank=debit(1500,1)
debit(bank)
