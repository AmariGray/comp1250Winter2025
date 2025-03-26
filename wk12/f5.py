import os

with open('test1.txt', 'a+') as fo:
    print(fo.read())  # since cursor is at the end of the file, read() outputs nothing
    lines_to_write = ['I love python\n', 'working with files are cool\n',
                      'i am awoke, I promise\n']
    fo.writelines(lines_to_write)
    # fo.seek(len(''.join(lines_to_write)))
    fo.seek(0)
    print(fo.read())


"""
what is the mode for fo object?
    appending PLUS
    what does PLUS mean?
        also can read
"""