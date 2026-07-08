def calculate_total(price, quantity):
    if price <= 0:
        return "invalid price"

    if quantity <= 0:
        return "invalid quantity"

    total = price * quantity
    return total

food_order = calculate_total