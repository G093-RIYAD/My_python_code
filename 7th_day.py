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

even_numbers = []
starting = 0
user_input = int(input("Limit : "))
while starting <= user_input:
    if even_num(starting):
        even_numbers.append(starting)
    starting = starting + 1
print(f"Even numbers : {even_numbers}")
print("Finished")
