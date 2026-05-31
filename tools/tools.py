from core.state import STATE
import random

def addition(nums):
    total=0
    for x in nums:
        total=total+x
    STATE["last_answer"]=total
    return total

def subtraction(nums):
    total=0
    for x in nums:
        total=total-x
    STATE["last_answer"]=total
    return total

def find_max(numbers):
    STATE["last_answer"]=max(numbers)
    return max(numbers)

def generate_random_numbers(count: int, min_val: int, max_val: int):
    x=[random.randint(min_val, max_val) for _ in range(count)]
    STATE["last_answer"]=x
    return x

def average(nums):
   total=0
   for x in nums:
    total=x+total
    average=total/len(nums)
    STATE["last_answer"]=average
    return average

def division(nums):
    total=0
    for x in nums:
        total=total/x
    STATE["last_answer"]=total
    return total

def multiplication(nums):
    total=1
    for x in nums:
        total=total*total
    STATE["last_answer"]=total
    return total

def area_square(length):
    STATE["last_answer"]=length*length
    return length*length

def area_circle(radius):
    area = 3.14 * radius * radius
    STATE["last_answer"]=area
    return area

def area_cube(length):
    STATE["last_answer"]=length*length*length
    return length*length*length