# how to define a set
set1={"apple","banana","orange"}
print(set1)

#how to combine a set along with a list
list1=[1,2,3,4,5]
set1.update(list1)
print(set1)

#how to combine a set along with a tuple
tuple1=("python","java","c++")
set1.add(tuple1)
print(set1)



#to clear the data in tha set without deleting the object ; .clear() function is used
set1.clear()
print(set1)

#to keep the set in ascending ordered ; sorted() function is used ; this method can only sort the numeric values
set2={9,5,6,8,7}
print(sorted(set2))



#frozen set ; mutable -> immutable
x=frozenset(set2)
print(x)

