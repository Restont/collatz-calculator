# Collatz Calculator

A Python script that checks the Collatz conjecture for any number. It counts the steps to reach 1 and finds the maximum number reached along the way.

## What is the Collatz conjecture?

The Collatz conjecture says that for any positive integer:
- If the number is even, divide it by 2
- If the number is odd, multiply it by 3 and add 1
- Repeat until you reach 1

Example: `6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1`

## Features

- Works with any positive integer
- Counts the number of steps
- Finds the maximum number reached
- Input validation (only numbers, positive only)
- Handles very large numbers

## How to run

1. Install Python
2. Run `collatz.py`
3. Enter any positive number
4. See the result

## Example
```
Any number: 27
Start: 27
Steps: 111
Max number: 9232
```
## Digit limit

By default, Python limits integer string conversion to **4300 digits**. If you want to use larger numbers, change the limit in the code:

```python
import sys
sys.set_int_max_str_digits(100000)
The number inside set_int_max_str_digits() is the new limit. Set it higher if needed (e.g. 1000000 for a million digits).
```
## author
Restont
