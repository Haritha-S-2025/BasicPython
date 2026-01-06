#String is a group of characters
message= "This is a sample "

#fetching the character by index
print(message[0])
print(message[-1])
print(message[-5])

#to traverse through the entire string
#first of all we need to find the length of the string
length=len(message)
for i in range(length):
    print(message[i])

#slicing : this will slice the string from the given starting index to the ending index ; also give the ending index+1
print(message[1:5])
#here the starting index is not specified; it will automatically fetch the starting index[0]
print(message[:5])

#concatenation - to combine more than one string(+)
greeting = "Hello " + message
print(greeting)

#case changing ; to uppercase, lowercase, capitalize
print(message.upper())
print(message.lower())
print(message.capitalize())

#Searching
print("that" in message)

#Replacing
newMessage=message.replace(" This","That")
print(newMessage)

#to capitalize the string; this will make the first character of each word in the string to capital
print(message.title())




