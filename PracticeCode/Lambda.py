from functools import reduce
numbers=[1,2,3,4,5]
even=filter(lambda l:l%2==0,numbers)
print(list(even))

numbers=[1,2,3,4,5]
evensquare=map(lambda l:l*l if l%2==0 else l ,numbers)
print(list(evensquare))

list=[1,2,3,4,5]
sum=reduce(lambda a,b:a+b,list)
print("sum of the numbers as ",sum)

list2=[2,3,4,5,8,6]
oddCube=reduce(lambda a,b:a+b,map(lambda m:m**3,filter(lambda f:f%2!=0,list2)))
print(oddCube)

subjectMarks={"science":90,"math":95,"physics":80}
maxmarks=max(subjectMarks,key=lambda k:subjectMarks[k])
print(maxmarks,subjectMarks[maxmarks])

minmarks=min(subjectMarks,key=lambda k:subjectMarks[k]) 
print(minmarks,subjectMarks[minmarks])