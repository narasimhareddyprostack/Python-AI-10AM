fp=open('abc.txt','w')

content = "This is a sample text file containing twenty words for testing file write operations in Python programming language."

fp.write(content)

print("New File created and written success!")

fp.close()