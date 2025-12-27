tea_menu = {"ice_tea": 15, "green_tea": 18, "lemon_tea": 20}
#print(f"This is lemon tea: {tea_menu["lemon_tea"]}") #this line prints the value of lemon_tea


#using exception we can handle errors better
try:
    tea_menu["ginger_tea"]
except KeyError:
    print("The item you are trying to access does not exist")
