
with open("test1.txt", 'r') as fo:
    first_5_chars = fo.read(5)
    print(first_5_chars)
    rest_of_line = fo.readline()
    print(repr(rest_of_line))
    print(fo.readlines())
    fo.seek(0)  # going back to the zeroth byte aka beginning of file
    print(fo.readline())
