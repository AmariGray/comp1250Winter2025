import os

dirname = "test1"
if not os.path.exists(dirname):
    os.mkdir(dirname)

print(os.curdir, os.pardir)
print(os.getcwd())

if os.path.exists(dirname) and not os.path.exists("test11"):
    os.rename(dirname, "test11")

if os.path.exists("test11"):
    os.rmdir("test11")
