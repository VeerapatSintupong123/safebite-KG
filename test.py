from transector import Transector

if __name__ == "__main__":
    transector = Transector(uri="", 
                            user="neo4j", 
                            password="")

    # Get all ingredients
    ingredients = transector.get_all_ingredients()
    print("All Ingredients:", ingredients[:10])

    # Get all foods
    foods = transector.get_all_foods()
    print("All Foods:", foods[:10])

    # Get ingredients for a specific food
    food_name = "pad thai"
    ingredients_for_food = transector.get_ingredients_for_food(food_name)
    print(f"Ingredients for {food_name}:", ingredients_for_food)

    # Get foods containing a specific ingredient
    ingredient_name = "flour"
    foods_with_ingredient = transector.get_foods_for_ingredient(ingredient_name)
    print(f"Foods with {ingredient_name}:", foods_with_ingredient)

    # Get synonyms for a specific ingredient
    ingredient_synonyms = transector.get_synonym_ingredients(ingredient_name)
    print(f"Synonyms for {ingredient_name}:", ingredient_synonyms)

    # Close the connection
    transector.close()
