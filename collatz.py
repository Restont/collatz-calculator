import sys
sys.set_int_max_str_digits(100000000)
steps = 0
number = int(input("Any number:"))
start = number
max_number = number
while number != 1:
    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1
    if number > max_number:
        max_number = number
    steps += 1
        
print(f"Start: {start}")
print(f"Steps: {steps}")
print(f"Max number: {max_number}")