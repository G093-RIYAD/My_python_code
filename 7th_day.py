#trying some while loop code
i = 1
while i < 6:
  print(i)
  i += 1

def even_num(number):
    if number % 2 == 0:
        return True
    else:
        return False
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

starting = 0
while starting < 1000:
    if even_num(starting):
        print(f"{starting} is Even")
    else:
        print(f"{starting} is Odd")
    starting = starting + 1

print("Finished")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
even_numbers = []
starting = 0
user_input = int(input("Limit : "))
while starting <= user_input:
    if even_num(starting):
        even_numbers.append(starting)
    starting = starting + 1
print(f"Even numbers : {even_numbers}")
print("Finished")

#Python For Loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)
