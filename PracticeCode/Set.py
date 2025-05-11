first={1,2,2,3,4,5,5}
#printing duplicate dont allowed
print(first)

#adding element
first.add(60)
print(first)
first.add(12)
print(first)

#discred 
first.discard(5)
print(first)

#empty
first.clear()
print(first)


#concate by union
second={1,2,3,4}
third={5,5,5,6,6,7,8}
fourth=second.union(third)
print(fourth)


#frozenset
fifth={1,2,3,4,frozenset({3,4,5,6,7,8})}
print(fifth)


#printing inner frozen and outher set
for ele in  fifth:
    if isinstance(ele,frozenset):
        for el in ele:
            print("inner elements",el)
    else:
        print("outer elements ",ele)
