def serve_tea(flavor):
    try:
        print(f"We are preparing your {flavor} tea...")
        if flavor == "unknown":
            raise ValueError(f"Sorry we don't know that flavor '{flavor}'.")
    except ValueError as e:
        print("Error:", e)
    else:
        print(f"{flavor} has been served")
        
    finally:
        print("Next customer please")

serve_tea("masala")
serve_tea("unknown")