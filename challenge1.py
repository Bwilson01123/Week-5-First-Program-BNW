# Ask the user to enter 5 numbers and store them in a list
nums = [int(num) for num in input ("Enter 5 numbers, use space to seperate: ").split(" ")]

# Print the list in reverse order
print (nums)
nums.reverse()
print (nums)

# Calculate the average of the numbers in the list
total=0
for num in nums:
    total = total + num
entries = len(nums)
print ("The average of the list is: "+ str(total/entries))

# Count how many numbers are greater than 10
amount = 0
for num in nums:
    if num > 10:
        amount=amount+1
print ("There are "+str(amount)+" of entries greater than 10")
# Create a function that checks if a number is prime
# Use the function to test every number in the list
# Create a dictionary where each number maps to its square
# Print the dictionary in a clean sentence format
# Use a loop to find the smallest number in the list
# Create a new list that only keeps even numbers
# Sort the new list from smallest to largest
# Write the results into a text file called results.txt
# Read the file and print its contents to the screen
# Handle errors if the file does not exist
# Create a menu that lets the user choose which task to run



'''
Documentation: 
https://python.plainenglish.io/efficiently-taking-multiple-inputs-in-python-234ff02088ac
https://towardsdatascience.com/reverse-python-list-ad10ad408021/#:~:text=Final%20Thoughts,go%20for%20reversed()%20function
https://bobbyhadz.com/blog/python-list-reverse-returns-none#:~:text=What%20is%20this?-,The%20list.,original%20object%20to%20return%20None%20.
https://www.digitalocean.com/community/tutorials/find-the-length-of-a-list-in-python



'''