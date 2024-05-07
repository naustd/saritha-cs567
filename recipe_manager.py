import json

class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = list(set(ingredients))
        self.instructions = instructions

    def __str__(self):
        return f"Recipe: {self.name}\nIngredients: {', '.join(self.ingredients)}\nInstructions: {self.instructions}"

class RecipeBook:
    def __init__(self):
        self.recipes = {}

    def add_recipe(self, recipe):
        if recipe.name not in self.recipes:
            self.recipes[recipe.name] = recipe
            print("Recipe added successfully.")
        else:
            print("Recipe already exists.")

    def remove_recipe(self, name):
        if name in self.recipes:
            del self.recipes[name]
            print("Recipe removed successfully.")
        else:
            print("Recipe not found.")

    def update_recipe(self, name, new_recipe):
        if name in self.recipes:
            old_recipe = self.recipes.pop(name)
            self.recipes[new_recipe.name] = new_recipe
            print("Recipe updated successfully.")
        else:
            print("Recipe not found.")

    def search_recipe(self, name):
        recipe = self.recipes.get(name, None)
        return recipe

    def list_recipes(self):
        recipes = []
        if self.recipes:
            recipes = list(self.recipes.values())
        return recipes

    def save_recipes(self):
        with open("recipes.json", "w") as file:
            json.dump({name: vars(recipe) for name, recipe in self.recipes.items()}, file)
        print("Recipes saved to file.")

    def load_recipes(self):
        try:
            with open("recipes.json", "r") as file:
                recipes = json.load(file)
                self.recipes = {name: Recipe(**data) for name, data in recipes.items()}
            print("Recipes loaded successfully.")
        except FileNotFoundError:
            print("No saved recipes found.")

def main():
    recipe_book = RecipeBook()
    recipe_book.load_recipes()

    while True:
        print("\nRecipe Manager Menu")
        print("1. Add Recipe")
        print("2. Remove Recipe")
        print("3. Update Recipe")
        print("4. Search Recipe")
        print("5. List All Recipes")
        print("6. Save Recipes")
        print("7. Load Recipes")
        print("8. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(',')
            instructions = input("Enter cooking instructions: ")
            recipe_book.add_recipe(Recipe(name, list(set(ingredients)), instructions))
        elif choice == '2':
            name = input("Enter recipe name to remove: ")
            recipe_book.remove_recipe(name)
        elif choice == '3':
            old_name = input("Enter the name of the recipe you want to update: ")
            new_name = input("Enter new recipe name: ")
            new_ingredients = input("Enter new ingredients (comma-separated): ").split(',')
            new_instructions = input("Enter new cooking instructions: ")
            new_recipe = Recipe(new_name, list(set(new_ingredients)), new_instructions)
            recipe_book.update_recipe(old_name, new_recipe)
        elif choice == '4':
            name = input("Enter recipe name to search: ")
            recipe_book.search_recipe(name)
        elif choice == '5':
            recipe_book.list_recipes()
        elif choice == '6':
            recipe_book.save_recipes()
        elif choice == '7':
            recipe_book.load_recipes()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()
