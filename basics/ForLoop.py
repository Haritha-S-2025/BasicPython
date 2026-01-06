#here start and stop values are defined; it prints 1 to 5
for i in range(1,6):
    print(i)
#here it prints from 0 to 5; the 6 mensioned here is the end vlue
for i in range(6):
    print(i)
#start vale is 1, end value is 7 : so it prints 1-7 ; and the step is 2 ; so it will incremented by 2; so the o/p is 1,3,5
for i in range(1,7,2):
    print(i)

#to print each charecters in a name
name="Haritha"
for i in name:
    print(i)


#Loop Control statements
name1="alexander"
for i in name1:
    if i=="x":
        #break #if a condition meets, it will exit from the loop
        #continue # if a condition meets, it will exit from the specific condition only
        pass # don't do anything
    print(i)
