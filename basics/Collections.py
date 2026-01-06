#collection ; group of objects
# 1) List; unordered collection of elements, there is a specific index value, and it is starts from 0

#how to create a list
list1=["apple",'a',2,2.5]
print(list1)

#Repeatitive list - it will print a specific element in number of times in the list
repList = [5]*10
print(repList)

#to access elements in the list ; specify the index of the element
print(list1[0])
print(list1[-1])

# some manipulation in list
#add a new element id the index 2
#insert method will insert a new value at the specified index
list1.insert(2,"python")
print(list1)

#append method will add the given value at the end of the list
list1.append("new value")
print(list1)

#index method will give the index of a value
print(list1.index("python"))
#print(list1.index("banana"))

#to sort the list . but we can only sort the numeric values
list2=[3,6,2,8,1,7]
list2.sort()
print(list2)

#reverse method will sort the list in descending order
list2.reverse()
print(list2)

#to find the occurance of an element
print(list1.count("python"))
print(list1.count("app"))


