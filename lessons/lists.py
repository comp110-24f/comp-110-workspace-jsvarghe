"""basic syntax of lists"""

# create an empty list

my_numbers: list[float] = []  # literal
# my_numbers: list[float] = list()  # constructor


# adding a value to a list
my_numbers.append(1.5)


# creating an already populated list
game_points: list[int] = [102, 86, 94]

# subscription notation/indexing
print(game_points[2])
last_game: int = game_points[2]
print(last_game)

# modifying by index
game_points[1] = 72
print(game_points)

# getting the length
len(game_points)

# removing an item
game_points.pop(1)
print(game_points)
