alpha={"name":"balaji","age":21,"name1":"balaji"}
print(alpha)
print(len(alpha))
print(type(alpha))

beta={"name":"balaji","age":21,"hobbies":"chatting","frnds":["balaji","kumar","rajesh"]}
#print(beta)

beta['name']="balaji"
print(beta)
beta.update({"hobbies":"singing"})
print(beta)

#clearmethod
beta.clear()
print(beta)
beta={"name":"balaji","age":21,"hobbies":"chatting","frnd":["balaji","kumar","rajesh"]}
print(beta)
#get method
a=beta.get("age")
print(a)
#items method
a=beta.items()
print(beta)
#key
a=beta.keys()
print(a)
#values
a=beta.values()
print(a)

#remove dict
beta={"name":"balaji","age":21,"hobbies":"chatting","frnd":["balaji","kumar","rajesh"]}
print(beta)
beta.pop("name")
print(beta)

#del
del beta["age"]
print(beta)

#loop dict
beta={"name":"balaji","age":21,"hobbies":"chatting","frnd":["balaji","kumar","rajesh"]}
#key names
for i in beta:
    print(i)

#values
for i in beta:
    print(beta[i])
    
#using values
for i in beta.values():
    print(i)
    
#using keys
for i in beta.keys():
    print(i)
    
#items
for i,j in beta.items():
    print(i,j)