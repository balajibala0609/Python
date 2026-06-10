#function with default parameter
def register(name,location,prefix="mr/mrs/miss"):
    if location == 'bangalore':
        print(prefix,name,"Has approved in",location)
    elif location == 'hydrabad':
        print(prefix,name,'Relocation the hydrabad',location)
    else:
        print("Business not approved")
register('cts','bangalore')
register('tcs','hydrabad','mr')
register("finish",'balaji')

