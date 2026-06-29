place=("salem","chennai","bengalore","hydrabad","chennai")
print(place)
print(type(place))

#slicing
print(place[0:2])
print(place[2:])

#tuple method
alpha=(1,45,87,98.36,78,45,50)
beta=alpha.count(45)
print(beta)
gamma=alpha.index(45)
print(gamma)

#append
department=('cse','mech','ece','eee')
dept=list(department)
dept.append('csbs')
dept1=tuple(dept)
print(dept1)

