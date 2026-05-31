from tools.tools import *

TOOLS = {
    "addition": addition,
    "subtraction": subtraction,
    "find_max": find_max,
    "generate_random_numbers": generate_random_numbers,
    "division": division,
    "multiplication": multiplication,
    "area_square": area_square,
    "area_circle": area_circle,
    "area_cube": area_cube,

    
}

TOOL_DESCRIPTIONS = {
    "subtraction": " subtracts two or more numbers. args: nums:int[]",
    "find_max": "Finds the largest number. args: nums:int[]",
    "generate_random_numbers": "Generates random numbers. args: count: int, min_val: int, max_val: int",
    "division": "Divides two or more numbers. arg: nums:int[]",
    "multiplication":"multiplies two or more numbers. arg: nums:int[]",
    "area_square": "multiplies length by length. arg: length:int",
    "area_circle": "finds the area of a circle arg: radius:int",
    "area_cube": "multiplies length by length by length. arg: length:int"
}