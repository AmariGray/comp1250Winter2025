fo = open("test1.txt", "r")
#content = fo.read()
#content = fo.readline()
while True:
    content = fo.readline()
    if not content:
        break
    print(repr(content))
fo.close()