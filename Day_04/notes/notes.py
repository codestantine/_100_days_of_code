import random

# random int
random_integer = random.randint(1, 10)
print(random_integer)

# random float
random_float_tiny = random.random()  # { 0.0 <-> 0.99999 }
print(random_float_tiny)

# random decimal between 0 - 5 ?
random_float_small = random_float_tiny * 5
print(f"small: {random_float_small}")

# lists
us_states = [
    "Alabama", "Alaska",
    "Arizona", "Arkansas",
    "California", "Colorado",
    "Connecticut", "Delaware",
    "Florida", "Georgia",
    "Hawaii", "Idaho",
    "Illinois", "Indiana",
    "Iowa", "Kansas",
    "Kentucky", "Louisiana",
    "Maine", "Maryland",
    "Massachusetts", "Michigan",
    "Minnesota", "Mississippi",
    "Missouri", "Montana",
    "Nebraska", "Nevada",
    "New Hampshire", "New Jersey",
    "New Mexico", "New York",
    "North Carolina", "North Dakota",
    "Ohio", "Oklahoma",
    "Oregon", "Pennsylvania",
    "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee",
    "Texas", "Utah",
    "Vermont", "Virginia",
    "Washington", "West Virginia",
    "Wisconsin", "Wyoming"
]
print(us_states)
print(len(us_states))
print(us_states[15])
print(us_states[17])

us_states[1] = "Pencilvania"
us_states.append("Angelaland")

# Adding another list to our list
us_states.extend(["Apples", "Oranges"])
print(us_states)

