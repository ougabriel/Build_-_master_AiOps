
#genrator basics

#using for loop:
# def coffee_type():
#     yield "cup1: Mocha"
#     yield "Cup2: Americano"
#     yield "Cup3: Latte"
#     yield "Cup4: Cappuccino"

# for cup in coffee_type():
#     print(cup)

################################################


#using next()
def coffee_type():
    yield "cup1: Mocha"
    yield "Cup2: Americano"
    yield "Cup3: Latte"
    yield "Cup4: Cappuccino"

coffee_order = coffee_type()

print(next(coffee_order))
print(next(coffee_order))
print(next(coffee_order))
print(next(coffee_order))

