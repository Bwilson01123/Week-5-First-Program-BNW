#ex1 make variable assign value
myVar = "AAAAAAAAAAAAHHHHHH"
myOtherVar = 67


#ex2 make variable assaign number
myNum = 67


#ex3 print test
print (f"\nHello World! " + myVar+ "\n")


#ex4 print values stored in "name" variable
name = "John Pork"
print (name)


#ex5 print a sentence usinng variable name
print (f"You got a call from: " + name + "\n")

#ex6 change value of variable then print again
change = 67
print (f"Funny number: " + str(change))
change = 420
print (f"Funny number: " + str(change)+ "\n")


#ex7 ask user for favorite animal
animal = input(f"What is your favorite animal? \n")
print (f"You chose "+str(animal) + " as your favorite\n")

#ex8 use variable created om example 1
if myOtherVar < 10:
    print ("this number is less than 10\n")
else:
    print ("This number is greater than 10\n")


