import sys

count = len(sys.argv)   #count is the amount of values in the file
total = 0
if len(sys.argv) <= 1:  #if the length of the file is less than or equal to 1
    print("no arguments were provided")
elif len(sys.argv) > 1: #if the length of the file is greater than 1
    while count > 1:
        count -= 1
        total += float(sys.argv[count])

print("Total is", total)
print(total / len(sys.argv))
