q = input("What is the answer to The Great Question of Life, the Universe and Everything? ")
if q=='42' or q=='forty-two' or q.lower()=='forty two' or '42' in q:
    print('Yes')
else:
    print("No")
