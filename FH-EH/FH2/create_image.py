fp1=open('loc.jpeg','rb')
image_data=fp1.read()

fp2=open('new_loc.jpeg','wb')
fp2.write(image_data)

print("New Image created!")

fp2.close()
fp1.close()