#print element
ftuple=("apple","banana","cheery")
print(ftuple)

#seperate elemets print
for i in ftuple:
    print(i)
 
#Getting length of tuples    
print(len(ftuple))

#multipling tuples
newtuple=ftuple*3
print(newtuple)

#nested tuples
ntuple=(1,2,3,4,("car","bike"))
print(ntuple)

for i in ntuple:
    print(i)
    
#print nested item through loop
for item in ntuple:
    if isinstance(item,tuple):
        for j in item:
            print(j)
    else:
        print(item)
        
#concate tuples
t1=(1,2,3)
t2=(4,5,6)
t3=(6,7,8,("ccar","bike"))
t4=t1+t2+t3
print(t4)

#through loop
for element in t4:
    if isinstance(element,tuple):
        for ie in element:
            print(ie)
    else:
        print(element)