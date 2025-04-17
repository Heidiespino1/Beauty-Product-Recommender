print("Welcome to the Beauty Product Recommender!")

# Sample product list
products = ["Moisturizer", "Cleanser", "Sunscreen", "Foundation", "Lipstick"]

# Simple product recommender
skin_type = input("What is your skin type? (oily, dry, normal): ").lower()

if skin_type == "oily":
    print("Recommended product: Oil-Free Moisturizer")
elif skin_type == "dry":
    print("Recommended product: Hydrating Cleanser")
elif skin_type == "normal":
    print("Recommended product: Daily Sunscreen")
else:
    print("Sorry, we don't have a recommendation for that skin type.")