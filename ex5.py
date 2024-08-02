name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

lbs_to_kg = 0.45
inch_to_m = 2.5

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.({height * inch_to_m} cm)")
print(f"He's {weight} pounds heavy.({weight * lbs_to_kg} kg)")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
