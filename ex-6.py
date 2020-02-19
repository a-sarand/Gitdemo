import os
fName = input ("provide a file name: \n")
if os.path.exists(fName):
   print(True)
else:
    print(False)


if os.path.isdir(fName):
   print(True)
else:
    print(False)

