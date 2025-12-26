name="Ajal"
for letter in name:
    print(letter)   

age=float(input("Enter your age: "))
if age>=18:         
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

name=input("Enter your name: ")
if name:           
    print("Hello, " + name + "!")   
else:
    print("You didn't enter a name.")

number=int(input("Enter a number: "))   
if number % 2 == 0:      
    print("The number is even.")    
else:
    print("The number is odd.")

first = input("Enter a word: ")
second = input("Enter another word: ")
words = first + " " + second + " "
print(words * 1000)