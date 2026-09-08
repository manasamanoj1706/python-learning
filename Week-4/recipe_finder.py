print("===== RECIPE FINDER =====")

recipes = {
    "pasta": ["pasta", "tomato", "cheese"],
    "omelette": ["egg", "onion", "salt"],
    "sandwich": ["bread", "cheese", "tomato"],
    "salad": ["lettuce", "tomato", "cucumber"]
}

ingredients = []

print("\nEnter the ingredients you have.")
print("Type 'done' when finished.")

while True:
    item = input("Ingredient: ").lower()

    if item == "done":
        break

    ingredients.append(item)

print("\n===== AVAILABLE RECIPES =====")

found = False

for recipe, required in recipes.items():
    if all(item in ingredients for item in required):
        print(f"🍴 {recipe.title()}")
        found = True

if not found:
    print("No complete recipe found.")

print("\nThanks for using Recipe Finder! 👩‍🍳")