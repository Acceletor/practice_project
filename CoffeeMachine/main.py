MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# resources
# water = resources["water"]
# milk = resources["milk"]
# coffee = resources["coffee"]
# money = 0


# TODO: 4. Check to use resources?
def check_resource(drink):

    x = MENU[drink]
    ingredient = x["ingredients"]
    used_water = 0
    used_coffee = 0
    used_milk = 0
    drink_cost = x["cost"]
    for _ in ingredient:
        if _ == "water":
            used_water = ingredient[_]
        if _ == "coffee":
            used_coffee = ingredient[_]
        if _ == "milk":
            used_milk = ingredient[_]
    return {"water" : used_water,
            "milk" : used_milk,
            "coffee" : used_coffee,
            "cost" : drink_cost}


# TODO: compare sufficient?
def compare(dict_to_use,water,milk,coffee):

    new_value = {}
    new_value["water"]=water - dict_to_use["water"]
    new_value["milk"]=milk - dict_to_use["milk"]
    new_value["coffee"]=coffee - dict_to_use["coffee"]

    for x in new_value:
        if new_value[x] < 1:
            print(f"Sorry there is not enough {x}.")
            return False

    return new_value


# TODO: 3. Print report.
def report(water, milk, coffee, money):
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}ml")
    print(f"Money: ${money}")


def coffeemachine():
    water=resources["water"]
    milk=resources["milk"]
    coffee=resources["coffee"]
    money = 0


    play = False

    while play == False:
        # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
        todo = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # TODO: 2. Turn off the Coffee Machine by entering "off' to the prompt.
        if todo == "off":
            play = True
        elif todo == "report":
            report(water, milk, coffee, money)
        else:
            if todo == "espresso" or todo == "latte" or todo == "cappuccino":
                ingredient_to_use = check_resource(todo)
                # compare
                x=compare(ingredient_to_use, water, milk, coffee)

                if x != False:
                    # TODO: 5. Process coins.
                    total=0
                    currency={
                        "quarter": 0.25,
                        "dime": 0.1,
                        "nickle": 0.05,
                        "penny": 0.01}
                    print("Please insert coins")
                    for _ in currency:
                        coins=int(input(f"How many {_}: "))
                        total += currency[_] * coins
                    cost_of_drink = ingredient_to_use["cost"]
                    # TODO: 6. Check transaction successful?
                    if cost_of_drink < total:
                        total -= cost_of_drink
                        format_total = "{:.2f}".format(total)
                        money += cost_of_drink
                        print(f"Here is ${format_total} your change.")
                        print(f"Here is you {todo}. Enjoy!!")
                        water=x["water"]
                        milk=x["milk"]
                        coffee=x["coffee"]
                    else:
                        print("Sorry that's not enough money. Money refund")
            else:
                print(f"{todo} is not in the menu")


coffeemachine()