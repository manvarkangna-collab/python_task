f=open("info.txt","w") # overwrite or create new file
f.write("hello studen\n")
f.write("welcome to python file handling\n")
f.writfe("learning is fun\n")
f.close()


f=open("info.txt","w") 
f.write("new content only.\n")
f.close()


f=open("info.txt","w")
f.write("this line is added at the end.\n")
f.close()


f=open("topics.txt","w")
lines=[
    "python programming\n",
    "file handling\n",
    "error handling\n",
    "exception handling\n",
]
f.writelines(lines)
f.close()



