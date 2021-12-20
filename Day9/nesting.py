capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary
# Example, tracking which cities you've visited in a different countries.

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a Dictionary in a Dictionary
# Example, tracking the above along with number of visits, etc.
expanded_travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 8,
    },
}

# Nesting a Dictionary inside of a List
dictionary_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 8,
    },
]
