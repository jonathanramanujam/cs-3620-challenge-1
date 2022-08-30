# Jonathan Ramanujam
# CS 3620
# Python Basics
# Part 2: List of Food Items

favorite_foods = [  'chicken coconut korma',
                    'sushi',
                    'cheeseburger',
                    'clam chowder in a bread bowl',
                    'crab legs'
                    ]

print("\nFavorite Food #3: " + favorite_foods[2])

print("\nAppending items...")
favorite_foods.append("shredded pork pozole")
favorite_foods.append("massaman curry")

print("\nList of Favorite Foods: ")
for food in favorite_foods:
    print(food)

print("\nInserting tacos...")
favorite_foods.insert(3, "tacos")

print("\nFinal List")
print(favorite_foods)
