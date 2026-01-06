#Tuple
#How to create a tuple ; there are different ways to create a tuple
myEmptyuple=()
print(myEmptyuple)

myTuple1=(1,"python",3.5)
print(myTuple1)

#we can create a tuple using a list; tuple is an inbuit function used for it
list=[1,"hii",2.5]
myTuple2=tuple(list)
print(myTuple2)

#if we need to create a repetitive tuple we use a coma after the specific element
repTuple=(1,)*5
print(repTuple)
