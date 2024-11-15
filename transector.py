from neo4j import GraphDatabase

class Transector:
    def __init__(self, uri, user, password):
        # Initialize the connection to the Neo4j database
        self.uri = uri
        self.user = user
        self.password = password
        self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))

    def _execute_transaction(self, query, parameters=None):
        """Executes a transaction with a query and optional parameters."""
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return [record for record in result]

    # 1. Return all Ingredients
    def get_all_ingredients(self):
        query = """
        MATCH (i:Ingredient)
        RETURN i.name AS ingredient
        """
        result = self._execute_transaction(query)
        return [record["ingredient"] for record in result]

    # 2. Return all Foods
    def get_all_foods(self):
        query = """
        MATCH (f:Food)
        RETURN f.name AS food
        """
        result = self._execute_transaction(query)
        return [record["food"] for record in result]

    # 3. Input food and return ingredients
    def get_ingredients_for_food(self, food_name):
        query = """
        MATCH (f:Food {name: $food_name})<-[:RECIPE]-(i:Ingredient)
        RETURN i.name AS ingredient
        """
        result = self._execute_transaction(query, parameters={"food_name": food_name})
        return [record["ingredient"] for record in result]

    # 4. Input ingredient and return possible foods
    def get_foods_for_ingredient(self, ingredient_name):
        query = """
        MATCH (f:Food)<-[:RECIPE]-(i:Ingredient {name: $ingredient_name})
        RETURN DISTINCT f.name AS food
        """
        result = self._execute_transaction(query, parameters={"ingredient_name": ingredient_name})
        return [record["food"] for record in result]

    # 5. Input ingredient and return synonym ingredients
    def get_synonym_ingredients(self, ingredient_name):
        query = """
        MATCH (i:Ingredient {name: $ingredient_name})-[:SYNONYM]->(syn:Ingredient)
        RETURN syn.name AS synonym
        """
        result = self._execute_transaction(query, parameters={"ingredient_name": ingredient_name})
        return [record["synonym"] for record in result]

    def close(self):
        """Close the connection to the database."""
        self.driver.close()