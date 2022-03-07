import requests

barcode = "033919000458"
# "049508001409"
# barcode = input("Please enter a barcode to search for data for a product.")
food_facts_url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
food_ingredients_data = requests.get(food_facts_url).json()["product"]["ingredients"]
ingredient_names = [ingredient["id"][3:] for ingredient in food_ingredients_data]
print(ingredient_names)
