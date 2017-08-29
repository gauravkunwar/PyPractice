"""file1=open("foo.txt","wb")
print"The name of the file is:",file1.name
print"Is file open or closed:",file1.closed
print"The file is in:",file1.mode"""
fo=open("foo.txt","wb")
fo.write("Python is a great langauage\n Yes its reaally great!!!")
fo.close()
