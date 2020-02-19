mylist = ["A", "B", "C"]
copied_list_1 = mylist

#step 2
copied_list_2 = mylist.copy()

#alternative
copied_list_2 = mylist[:]

#step 3
mylist[1] = 'x'

print(mylist)
print(copied_list_1)
print(copied_list_2)
