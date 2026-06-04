#function parameter
def hiring(qual,ref):
    if qual =='Ug' and ref=='hr':
        print("You are hired in US Based Project")
    elif qual=='Pg' and ref=='Team lead':
        print("You are hired in kpo company")
    else:
        print("You are Hired")
    hiring(qual='Ug',ref='hr')
    hiring(qual='Pg',ref='Team lead')
    
    
#def hiring(qual,ref):
 #   if qual =='ug' and ref=='hr':
  #      print("You are hired in US Based Project")
   # elif qual == 'Pg' and ref=='Team lead':
    #    print("You are hired in KPo company") 
    #else:
     #   print("You are Hired")
#hiring(qual='ug',ref='hr')
#hiring(qual='pg',ref='Team lead')