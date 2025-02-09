file = input("Enter name of file: ")

l = file.split(".")

if len(l)==1:
    print("application/octet-stream")


elif l[-1] == 'gif':
    print("image/gif")

elif l[-1] == 'jpg' or l[-1] == 'jpeg':
    print("image/jpeg")

elif l[-1] == 'png':
    print("image/png")

elif l[-1].lower().rstrip() == 'pdf':
    print("application/pdf")

elif l[-1] == 'txt':
    print("text/plain")

elif l[-1] == 'zip':
    print("application/zip")

else:
    print("application/octet-stream")
