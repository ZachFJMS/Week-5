number = input("Enter a number: ")  #number will store an inputted value

number = int(number)    #number is changed to an integer

print("The numbered entered was", number)

if (number % 2) == 0:
    print("That is an even number")
else:
    print("That is an odd number")

if (number % 10) == 0:
    print("The number is divisible by 10")
