# python-arrayCollections_b-cw
#
# Problem 1:
# Create a function with the variable below. After you create the variable do the instructions below that.

arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]

# a) Print the 3rd element of the numberList.
print(arrayForProblem2[2])

# b) Print the size of the array
print(len(arrayForProblem2))

# c) Delete the second element.
del arrayForProblem2[1]
print (arrayForProblem2)

# d) Print the 3rd element.
print (arrayForProblem2[2])

#  Problem 2:
# We will keep having this problem until EVERYONE gets it right without help
#   Create a function that has a loop that quits with ‘q’.
#     If the user doesn't enter 'q', ask them to input another string.

userInput = ""
while userInput != "q":
    userInput = input("Enter a word or q to quit.")

# Problem 3:
# Create a function that contains a collection of
# information for the following. After you create the collection do the instructions below that.

# Jonathan/John
# Michael/Mike
# William/Bill
# Robert/Rob
# ```
# a) Print the collection
#
# b) Print William's nickname


#  Problem 4:
# Create an array of 5 numbers.
# Using a loop, print the elements in the array reverse order.
# Do not use a function
#
numberarray = [1, 2, 3, 4, 5]

for x in reversed(numberarray):
    print (x)


# ### Problem 5:
# Create a function that will have a hard coded array then ask the user for a number.
# Use the userInput to state how many numbers in an array are higher, lower, or equal to it.
def loverGirl(usernumber):
    highercount = 0
    lowercount = 0
    equalTo = 0
    lovernumbers = [2, 5, 7, 3, 1]
    for numero in lovernumbers:
        if numero > usernumber:
            highercount = highercount + 1

        if numero < usernumber:
            lowercount = lowercount + 1

        if numero == usernumber:
            equalTo = equalTo + 1

    print(f'{highercount} number(s) in this array are higher than {usernumber}.')
    print(f'{lowercount} number(s) in this array are lower than {usernumber}.')
    print(f'{equalTo} number(s) in this array are equal to {usernumber}.')

userNumber = int(input("Enter a number."))
loverGirl(userNumber)