#Create an empty list called my_list.
my_list = []
#Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#print(my_list) output [10, 20, 30, 40]
#Insert the value 15 at the second position in the list.
my_list.insert (1,15)
#print(my_list)
#Extend my_list with another list: [50, 60, 70].
list2 = [50, 60, 70]
#print(list2)
my_list.extend(list2)
#print(my_list) # Output [10, 15, 20, 30, 40, 50, 60, 70]
#Remove the last element from my_list.
#my_list.remove(70)
my_list.pop()
#print(my_list)
#Sort my_list in ascending order.
my_list.sort()
#print(my_list)
#Find and print the index of the value 30 in my_list.
index = my_list.index (30)
print(f"The index of 30:", {index})