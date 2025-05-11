list=[1,2,3,4,5]
for i in list:
    print(i)
print(list)

#square of items in list
squared=[x**2 for x in list]  
print(squared)

#reverse the list
squared.reverse()
print(squared)

#sorting 
newlist=[3,4,2,5,7,54,3,3]
newlist.sort()
print(newlist)


#insert
strlist=["car","bike","aroplane","boat",'car','bike']
strlist.insert(6,'railway')
print(strlist)

#print
for i in strlist:
    print(i)
    
    
strlist.insert(0,'bike')
print(strlist)

#remove last elemet
strlist.pop()
print(strlist)

#renameitem
strlist[1]='helicptoer'
print(strlist)

#get count same element
print(strlist.count('bike'))
