import os

folderName = input("Type the name of the folder: ")
folderDir = input("Type the directory of the folder: ")

path = os.path.join(folderDir, folderName)
os.mkdir(path)
print(f"'{folderName}' has been created in {folderDir}")
