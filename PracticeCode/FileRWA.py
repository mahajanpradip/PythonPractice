file=open("D://Demo.txt","w")
file.write("This is Demo text")
file.close()
print("File writen sucess")

filer=open("D://Demo.txt","r")
content=filer.read()
print("Content in file => : ",content)
filer.close()


filea=open("D://Demo.txt","a")
filea.write("\n Again this is Demo file")
filea.close()
print("Text added")

with open("D://Demo.txt","r") as a:
    text=a.read()
    print(text)
    