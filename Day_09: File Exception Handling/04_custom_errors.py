def brewTea(flavor):
    if flavor not in ("ginger", "lemon", "green"):
        raise ValueError("Unknown tea flavor.")
    print(f"Brewing your {flavor} tea")


brewTea("black")