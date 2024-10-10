"""the purpose of this program is to calculate total cost based on how many guests are attending"""

__author__: str = "730677312"


def main_planner(guests: int) -> None:
    """Purpose is to bring all values together"""
    print("A Cozy Tea Party for " + str(guests) + " people")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


"""Used all functions in this function to bring values together and compute the total cost """

"""print the cost function with the values of tea count and treat count automatically being computed using the corresponding functions"""


def tea_bags(people: int) -> int:
    """to store amount of tea bags needed depending on how many people there are"""
    return int(people * 2)


"""calculates tea bags based on amount of people inputed"""


def treats(people: int) -> int:
    """purpose of this function is to spit out the amount of treats needed based on tea bags"""
    return int(tea_bags(people=people) * 1.5)


""" calculates treats based on tea bags"""


def cost(tea_count: int, treat_count: int) -> float:
    """this function is compute the cost of the tea bags and treats combined"""

    return tea_count * 0.5 + treat_count * 0.75


"""returns the cost of tea and treats using the values that were put in """

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
"""code used to get input from user"""
