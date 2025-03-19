import os

values = os.listdir(os.getcwd())
# values = os.listdir(os.pardir)
print(values)

# list comprehensions

files = list()
folders = list()

for file_or_folder in values:
    # print("Dir?", os.path.isdir(file_or_folder))
    # print("File?", os.path.isfile(file_or_folder))
    if os.path.isdir(file_or_folder):
        folders.append(file_or_folder)
    elif os.path.isfile(file_or_folder):
        files.append(file_or_folder)

print(files, folders)


data_folders = [v for v in values if os.path.isdir(v) ]
data_files = [v for v in values if os.path.isfile(v)]


print(data_folders)
print(data_files)