from core.state import STATE

def cart_add(item: str, cost: int):
    STATE["cart"].append({
        "name": item,
        "price": cost
    })
    return f"Added {item} for ${cost}"

def cart_total():
    return sum(entry["price"] for entry in STATE["cart"])

def cart_list():
    return STATE["cart"]