from core.state import STATE
import random

def addition(nums):
    total=0
    for x in nums:
        total=total+x
    return total

def subtraction(nums):
    total=0
    for x in nums:
        total=total-x
    return total

def find_max(numbers):
    return max(numbers)

def generate_random_numbers(count: int, min_val: int, max_val: int):
    return [random.randint(min_val, max_val) for _ in range(count)]

def average(nums):
   total=0
   for x in nums:
    total=x+total
    average=total/len(nums)
    return average

def division(nums):
    total=0
    for x in nums:
        total=total/x
    return total

def multiplication(nums):
    total=0
    for x in nums:
        total=total*total
    return total

def area_square(length):
    return length*length

def area_circle(radius):
    area = 3.14 * radius * radius
    return area

def area_cube(length):
    return length*length*length