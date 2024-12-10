#Task - searching in strings using startswith() and in methods

girl_names = ['Emily', 'Ava', 'Serenity', 'Claire', 'Sophia', 'Sarah', 'Ashley', 'Chaya', 'Abigail', 'Zoe', 'Leah', 'Ava', 'Olivia', 'Emma', 'Chloe', 'Sophia', 'Aaliyah', 'Angela', 'Camila', 'Savannah', 'Serenity', 'Chloe', 'Fatoumata']

# Store a list of girl_names that start with s: names_with_s
names_with_s = [name for name in girl_names if name.lower().startswith('s')]

print(names_with_s)

# Store a list of girl_names that contain angel: names_with_angel
names_with_angel = [name for name in girl_names if 'angel' in name.lower()]

print(names_with_angel)