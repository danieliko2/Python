import os   # Create file inside folder (overwrite folder)
from shutil import rmtree
print("hello world")
if os.path.exists("newFolder"):
    rmtree("newFolder")
os.mkdir("newFolder")
with open("newFolder/newFile.txt", "w") as newFile:
    newFile.write("written to new file")