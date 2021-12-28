import os
for file in os.listdir():
    if file == "txtfile.txt":
        os.remove(file)
with open("txtfile.txt", 'w') as txtfile:
    txtfile.write("line1\n")
with open("txtfile.txt", 'a') as txtfile:
    txtfile.write("line2")