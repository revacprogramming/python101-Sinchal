# Loops & Iterators

largest = 0
smallest = 0
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        num=int(num)
        largest=num if num > largest or largest == 0 else largest
        smallest=num if num<smallest or smallest == 0 else smallest
        
    except ValueError:
        print("Invalid input")

print ("Maximum is",largest)
print("Minimum is",smallest)