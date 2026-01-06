"""data="this is haritha"
i=0
#count how many vowels in this sentence
count=0
#here we need to find the length of the given data; len() is the function used to get the length of a string
length=len(data)
while i<length:
    if data[i]=="a" or data[i]=="e" or data[i]=="i" or data[i]=="o" or data[i]=="u":
        count=count+1 # the count is only for the if block
    i=i+1
print(count)"""
#suppose while condition is false, it will go with the else block
data="this is haritha"
i=0
#count how many vowels in this sentence
count=0
#here we need to find the length of the given data; len() is the function used to get the length of a string
length=len(data)
while i<length:
    if data[i]=="a" or data[i]=="e" or data[i]=="i" or data[i]=="o" or data[i]=="u":
        count=count+1 # the count is only for the if block
    i=i+1
else:
    print("execution is completed")
print("number of vowels in the data is ",count)




