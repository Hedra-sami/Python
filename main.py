# Print the greeting below
print("Hello, Ship That Code!")

#Lesson Two
name = input()
age = input()
print("Hi, "+name+"! You are "+age+" years old.")

#Lesson 3
width = int(input())
height = int(input())

# Print the area on line 1 and the perimeter on line 2
print(width*height)
print(2*(width+height))

#Lesson 4
# Read two numbers and print their sum.
a = input()
b = input()
# Convert and add
a=int(a)
b=int(b)
print(a+b)


#Lesson 5
num = int(input())
# Check the sign and print the matching word
if num > 0 :
  print("positive")
elif num < 0 :
  print("negative")
else :
  print("zero")

#Lesson 6
score = int(input())
# Print the letter grade for this score
if score >= 90 :
  print("A")
elif 80<=score<=89 :
  print("B")
elif 70<=score<=79 :
  print("C")
elif 60<=score<=69 :
  print("D")
else :
  print("F")

#Lesson 7
year = int(input())
# Determine and print 'leap' or 'not leap'
if ((year % 4 == 0) and ((year % 100 != 0)) or(year % 400 == 0)) :
  print("leap")
else :
  print("not leap")


#Lesson 8
n = int(input())
# Print the multiplication table from 1 to 10
for i in range(1,11):
  mul = n*i
  print(f"{n} x {i} = {mul}")


#Lesson 9
total = 0
# Read numbers and accumulate them until you see 0
while True :
  x = int(input())
  if x != 0 :
    total = total + x
  else :
    break

print(total)


#Lesson 10
n = int(input())
# Print a right-aligned triangle of stars
for row in range(1,n+1):
  spaces = " " * (n-row)
  stars = "*" * row
  print(spaces+stars)


#Lesson 11
text = input()
# Print the reversed string
print(text[::-1])

#Lesson 12
text = input()
# Count vowels (case insensitive)
count =0
for char in text :
  if char.lower() in ("a","e","i","o","u"):
    count=count+1
  else :
    continue
print(count)


#Lesson 13
item = input()
qty = int(input())
price = float(input())
# Print the 3-line receipt
Total = qty*price

print(f"Item: {item}")
print(f"Quantity: {qty}")
print(f"Total: ${Total:.2F}")