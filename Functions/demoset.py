IT_company={'cts','tcs','cts','wipro','accenture'}
print(IT_company)

#set constractor
places=set(('bengalore','chennai','hydrabed'))
print(places)

#update set
cosmo={'balaji','priya','anusha','samantha'}
cosmo.update('trisha')
print(cosmo)

#update set
alpha={'vijay','rajmohan','balaji','arunraj'}
li=['sengattaiyan']
alpha.update(li)
print(alpha)

#remove set
alpha.remove('balaji')
print(alpha)
alpha.discard(1)
print(alpha)

#pop
a={'annamalai','sathish',29,30}
a1=a.pop()
print(a1)
print(a)

#access set
a={'annamalai','sathish',29,30}
for i in a:
    print(i)
    
#check the set
am={'annamalai','sathish',29,30}
print('sathish'in am)
    