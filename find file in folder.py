import os # find file in folder
for filename in os.listdir():
    if filename == "script.py":
        print(filename)