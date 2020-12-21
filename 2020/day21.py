from aoc.tools import read_input

test = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
""".splitlines()

data = read_input("input")

def parse_data(data):
    food_list = []
    for l in data:
        l = l.replace(",", "")
        food, allergy = l.split(" (contains ")
        food = food.split()
        allergy = allergy.split(")")[0].split()
        food_list.append((food, allergy))
    return food_list

food_list = parse_data(data)

ingredient_dict = {}
allergen_dict = {}

for item in food_list:
    allergens = item[-1]
    ingredients = set(item[0])
    for ingredient in ingredients:
        ingredient_dict[ingredient] = ingredient_dict[ingredient] + 1 if ingredient in ingredient_dict else 1
    for allergen in allergens:
        if allergen in allergen_dict:
            allergen_dict[allergen] = allergen_dict[allergen] & ingredients  # intersection
        else:
            allergen_dict[allergen] = ingredients

maybe = set()
for allergen in allergen_dict:
    maybe = maybe | allergen_dict[allergen]  #union

count = sum(
    value for word, value in ingredient_dict.items() if word not in maybe)
print(count)

confirmed = []
while len(confirmed) < len(allergen_dict):
    for allergen, ingredient in allergen_dict.items():
        if len(ingredient) == 1 and allergen not in confirmed:
            confirmed.append(allergen)
            # update dict
            for key, items in allergen_dict.items():
                if key != allergen:
                    allergen_dict[key] = items - ingredient

canonical = ",".join(
    ingredient.pop() for allergen, ingredient in sorted(allergen_dict.items()))

print(canonical)