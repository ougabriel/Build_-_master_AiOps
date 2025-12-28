class InvalidTeaError(Exception):
    pass

def bill(flavor, cups):
    menu = {"ginger": 12, "lemon": 15, "green": 10 }
    try:
        if flavor not in menu:
             raise InvalidTeaError("We do not have your tea on the menu.")
        if not isinstance(cups, int):
             raise TypeError("Value must be an integer.")
    
        total = menu[flavor] * cups
        print(f"Your bill for {flavor} tea and {cups} cups is: £{total}")

    except Exception as e:
        print("Error:", e)
    
    finally:
        print("Welcome to our Tea Shop.")
    

#bill("ginger", 3)
bill("honey", 2)
#bill("lemon", "five")
