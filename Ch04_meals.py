starters = {
    "Potato Pancakes": 7.99,
    "Salami Platter": 10.29,
    "Brezel": 6.99,
    "Maultaschen": 9.99,
    "Fried Potatoes": 4.99
}

mains = {
    "Braised Beef Short Ribs": 18.99,
    "Paprika Beef Goulash": 15.5,
    "Jager Schnitzel": 16.99,
    "House-mase Bratwurst": 11.99,
    "Kasespatzle": 14.99,
    "German Ravioli": 12.79,
    "Curry Wurst": 10.99
}

desserts = {
    "Chilled Chocolate Fondant": 7.9,
    "Pepermint Crisp Tart": 5.9,
    "Ginger Cobbler": 6.9,
    
}

beers = {
    "Stigel Radler": 6.9,
    "Munich Lager": 7.9,
    "Kong Ludwig Weissbier": 8.9,
    "Warsteiner Punkel": 7.5,
}
max_starters = max(starters, key = starters.get)
max_mains = max(mains, key = mains.get)
max_desserts = max(desserts, key = desserts.get)
max_beers = max(beers, key = beers.get)
meals = {
    "starters":max_starters,
    "mains":max_mains,
    "desserts":max_desserts,
    "beers": max_beers
    }
total_cost = 0.1 * (starters.get(max_starters) + mains.get(max_mains)
    + desserts.get(max_desserts) + beers.get(max_beers))
print(meals)
print(total_cost)

# if you want to see the keys of the dictionary in the list: keys = list(starters.keys())
# if you want to see the keys of the dictionary in the list: values = list(starters.values())