dicct={
    "name":"pradip",
    "age":23,
    "address":"pune"
}
print(dicct)

#print through loop
for k,v in dicct.items():
    print(k,v)
  
#new key value pair    
dicct["parmanant address"]="jalgaon"
print(dicct)

#modify address
dicct["address"]="sangvi"
print(dicct)


#nested dict
nestdict={
    "person1":{"name":"abc","age":22},
    "person2":{"name":"xyz","age":23}
}
print(nestdict)


print("========================================")
for k,v in nestdict.items():
    if isinstance(v,dict):
        print(f"details of {k}")
        for ik,iv in v.items():
            print(f"{ik},{iv}")
    else:
        print(f"{k},{v}")