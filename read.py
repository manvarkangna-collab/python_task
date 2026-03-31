f=open("myfile.txt","r")
data=f.read()  # read whole file
print("file content:",data)
f.close()


f=open("myfile.txt","r")
data=f.read(10)  # first 10 characters
print("first part:",data)
f.close()


f=open("myfile.txt","r")
line1=f.readine()
line2=f.readine()
line3=f.readine()
print("line1:",line1)
print("line2:",line2)
print("line3:",line3)
f.close()


f=open("myfile.txt","r")
line1=f.readines()
print("list of lines:",lines)
print("number of lines:",len(lines))


#reads specific line in file
f=open("myfile.txt","r")
line1=f.readines()
print(lines[1].strip())
f.close()
