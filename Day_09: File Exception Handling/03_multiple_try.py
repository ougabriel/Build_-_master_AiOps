def process_order(item, quantity):
    try:
        price = {"ginger_tea": 15}[item]
        cost = price * quantity
        print(f"Total cost equals {cost}")
    except KeyError:
        print("The tea order is not available.")
    except ValueError:
        print("The quantity amount should be in numbers.")
process_order("green_tea", 13)
process_order("ginger_tea", "eighteen")