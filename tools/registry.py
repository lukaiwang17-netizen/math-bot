from tools.tools import *

TOOLS = {
    "cart_add": cart_add,
    "cart_total": cart_total,
    "cart_list": cart_list,
}

TOOL_DESCRIPTIONS = {
    "cart_add": "Add an item to the cart. args: item:str, cost:int",
    "cart_total": "Return total cost of all items in cart. args: none",
    "cart_list": "Return all items currently in cart. args: none",
}