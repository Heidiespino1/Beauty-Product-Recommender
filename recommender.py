print("✨ Welcome to the Beauty Product Recommender ✨\n")

# Available options
skin_types = ["oily", "dry", "normal", "combination"]
skin_concerns = ["acne", "sensitive", "aging"]
product_types = ["moisturizer", "cleanser", "sunscreen", "foundation", "lipstick"]

# Collect user input
skin_type = input(f"What is your skin type? ({', '.join(skin_types)}): ").lower()
concern = input(f"Do you have any specific skin concern? ({', '.join(skin_concerns)} or 'none'): ").lower()
product = input(f"What kind of product are you looking for? ({', '.join(product_types)}): ").lower()

# Recommendation logic
def get_recommendation(skin_type, concern, product):
    if product == "moisturizer":
        if skin_type == "oily":
            return "Oil-Free Gel Moisturizer"
        elif skin_type == "dry":
            return "Ultra Hydrating Cream"
        elif concern == "aging":
            return "Anti-Aging Moisturizer with Retinol"
        else:
            return "Daily Lightweight Moisturizer"

    elif product == "cleanser":
        if concern == "acne":
            return "Salicylic Acid Cleanser"
        elif skin_type == "sensitive":
            return "Fragrance-Free Gentle Cleanser"
        else:
            return "Foaming Daily Cleanser"

    elif product == "sunscreen":
        if skin_type == "oily":
            return "Matte Finish Sunscreen SPF 50"
        elif concern == "sensitive":
            return "Mineral-Based Sunscreen"
        else:
            return "Broad Spectrum SPF 30 Sunscreen"

    elif product == "foundation":
        return "Lightweight Foundation with SPF"

    elif product == "lipstick":
        return "Hydrating Lipstick with Vitamin E"

    else:
        return "Sorry, we don’t have a recommendation for that combination."

# Output
recommendation = get_recommendation(skin_type, concern, product)
print(f"\n💄 Recommended Product: {recommendation}")