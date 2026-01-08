class OutOfIngredientError(Exception):
    pass

def ingredients(milk, sugar):
    if milk == 0 or sugar == 0: 
        raise OutOfIngredientError("We are out of stock, please reorder.")
    
    print("Stock check is complete...")


ingredients(2, 3)
ingredients(0, 2)
