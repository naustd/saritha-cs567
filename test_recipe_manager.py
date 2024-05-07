import unittest
from recipe_manager import Recipe, RecipeBook
import os

class TestRecipeManager(unittest.TestCase):

    def setUp(self):
        self.recipe_book = RecipeBook()
        self.recipe_book.add_recipe(Recipe("Recipe1", ["Ingredient1", "Ingredient2"], "Instructions 1"))
        self.recipe_book.add_recipe(Recipe("Recipe2", ["Ingredient3", "Ingredient4"], "Instructions 2"))

    def test_remove_recipe(self):
        self.recipe_book.remove_recipe("Recipe1")
        self.assertNotIn("Recipe1", self.recipe_book.recipes)

    def test_update_recipe(self):
        new_recipe = Recipe("New Recipe", ["New Ingredient1", "New Ingredient2"], "New Instructions")
        self.recipe_book.update_recipe("Recipe2", new_recipe)
        self.assertIn("New Recipe", self.recipe_book.recipes)
        self.assertNotIn("Recipe2", self.recipe_book.recipes)

    def test_search_recipe(self):
        recipe = self.recipe_book.search_recipe("Non-existent Recipe")
        self.assertIsNone(recipe)

    def test_list_recipes(self):
        recipes = self.recipe_book.list_recipes()
        self.assertGreater(len(recipes), 0)

    def test_save_load_recipes(self):
        self.recipe_book.save_recipes()
        self.assertTrue(os.path.exists("recipes.json"))

        self.recipe_book = RecipeBook()
        self.recipe_book.load_recipes()
        self.assertEqual(len(self.recipe_book.recipes), 2)

    def tearDown(self):
        if os.path.exists("recipes.json"):
            os.remove("recipes.json")

if __name__ == '__main__':
    unittest.main()
